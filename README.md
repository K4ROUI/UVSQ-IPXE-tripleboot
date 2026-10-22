# TER Diskless iPXE Triple-Boot

## 1. Project overview

This project provides a diskless network boot environment for three operating
systems:

1. Ubuntu Live
2. Debian Live
3. Windows PE

The client machine does not need an operating system or a local installation
to start one of these entries. The PXE client obtains iPXE through DHCP/TFTP,
then downloads the selected kernel, initrd, ISO, or Windows boot files over
HTTP.

This configuration is intended for a private lab network. It is not a
replacement for a DHCP service in a production network.

## 2. Network architecture

```text
PXE client
    |
    | DHCP + TFTP: iPXE firmware
    v
Tiny PXE Server on the Windows host
    |
    | HTTP: menu, kernels, initrds, ISO files, and Windows PE files
    v
Diskless operating-system session
```

The menu uses `${dhcp-server}` instead of a fixed IP address. The same files
can therefore be used when the PXE server receives a different address from
the lab network.

## 3. Repository layout

| Path | Purpose |
| --- | --- |
| `config.ini` | Tiny PXE Server DHCP, TFTP, and HTTP configuration |
| `menu.ipxe` | Diskless triple-boot menu |
| `ipxe.efi` | iPXE UEFI loader |
| `casper/` | Ubuntu kernel, initrd, and Live ISO |
| `debian/` | Debian kernel, initrd, and Live ISO |
| `windows/` | Windows PE boot files and wimboot |
| `files/` | Additional iPXE, PXELINUX, GRUB, and Windows helpers |
| `pxesrv.exe` | Tiny PXE Server executable |

## 4. Requirements

- A Windows PXE server host.
- A client machine or virtual machine with PXE boot enabled.
- A private Ethernet or virtual network shared by the server and client.
- DHCP access on that network.
- The boot files already present in this repository:
  - `casper/ubuntu.iso`, `casper/vmlinuz`, and `casper/initrd`
  - `debian/debian-live.iso`, `debian/vmlinuz`, and `debian/initrd.img`
  - `windows/wimboot`, `windows/bcd`, `windows/boot.sdi`, and `windows/boot.wim`

Do not run a second DHCP server on the same isolated lab network. If another
DHCP server is required, use Tiny PXE Server in proxy-DHCP mode and adapt the
network settings to that environment.

## 5. Tiny PXE Server configuration

`config.ini` is configured to:

- serve the repository directory as the HTTP/TFTP root;
- send `ipxe.efi` to UEFI clients;
- use `menu.ipxe` as the iPXE chain file;
- enable the HTTP server;
- start automatically;
- bind to the selected network interface.

Before starting the server, verify that the `root` setting points to the
directory containing `config.ini`. If the repository is moved, update this
line:

```ini
root=C:\studies\TER
```

Start `pxesrv.exe`, select the correct network interface, and confirm that
DHCP, TFTP, and HTTP are active.

## 6. Client boot procedure

1. Connect the client and server to the same isolated network.
2. Enable network/PXE boot in the client firmware.
3. Select the UEFI network boot entry.
4. Wait for the iPXE menu.
5. Select Ubuntu Live, Debian Live, or Windows PE.

The menu is defined in `menu.ipxe`. It first sets:

```ipxe
set boot-url http://${dhcp-server}
```

This makes all subsequent downloads use the address announced by the PXE
server.

## 7. Boot entries

### 7.1 Ubuntu Live

The Ubuntu entry downloads the kernel and initrd over HTTP. The kernel then
retrieves `casper/ubuntu.iso` from the same server using the `url=` parameter.
The `ip=dhcp` option configures networking inside the live session.

### 7.2 Debian Live

The Debian entry downloads `debian/vmlinuz` and `debian/initrd.img`. The live
environment retrieves `debian/debian-live.iso` using the `fetch=` parameter.

### 7.3 Windows PE

The Windows entry uses `wimboot` to load the Windows PE environment. It
downloads the BCD store, boot sector support file, and Windows boot image from
the `windows/` directory. No Windows installation is written to the client
disk by this menu.

## 8. Protocols used

| Protocol | Use |
| --- | --- |
| DHCP | Provides network settings and the initial PXE boot filename |
| TFTP | Transfers the initial iPXE EFI loader |
| HTTP | Transfers the iPXE menu, Linux boot files, ISO files, and Windows PE files |
| iPXE | Executes the menu and starts each network boot path |

The operating-system images are deliberately transferred over HTTP rather than
TFTP because HTTP is better suited to large kernel, initrd, and ISO files.

## 9. Troubleshooting

### The client receives no PXE response

- Confirm that the client and server are on the same network.
- Disable competing DHCP services on the lab network.
- Confirm that the correct network interface is selected in Tiny PXE Server.
- Check that `ipxe.efi` exists in the configured root directory.

### The iPXE menu does not load

- Open `http://SERVER-IP/menu.ipxe` from another machine on the lab network.
- Confirm that `altfilename=menu.ipxe` is present in `config.ini`.
- Check the Tiny PXE Server log for the requested filename.

### Ubuntu or Debian stops while loading

- Check that the ISO, kernel, and initrd files exist in the expected directory.
- Confirm that the client received an IP address.
- Check that the HTTP server can serve the complete ISO file.

### Windows PE does not start

- Confirm that `windows/wimboot`, `windows/bcd`, `windows/boot.sdi`, and
  `windows/boot.wim` are present.
- Verify that the BCD file matches the Windows PE image.
- Check the HTTP log for failed or incomplete downloads.

## 10. Validation checklist

- [ ] Tiny PXE Server starts without a root-directory error.
- [ ] A UEFI client receives `ipxe.efi`.
- [ ] The iPXE menu displays all three entries.
- [ ] Ubuntu Live reaches its live environment.
- [ ] Debian Live reaches its live environment.
- [ ] Windows PE reaches the WinPE environment.
- [ ] No client operating-system installation is required.
- [ ] No client disk is used as the boot source.

## 11. Scope and limitations

This project is a network-boot demonstration and lab configuration. It
requires compatible live images and a network that can deliver large files
reliably. Persistence, unattended installation, secure boot signing, and
production DHCP integration are outside the current scope.
