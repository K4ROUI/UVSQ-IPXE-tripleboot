"""Vérifications statiques de config.ini et menu.ipxe, sans matériel PXE."""

from configparser import ConfigParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class IPXEConfigTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menu = (ROOT / "menu.ipxe").read_text(encoding="utf-8")
        cls.config = ConfigParser(interpolation=None)
        cls.config.read(ROOT / "config.ini", encoding="utf-8")

    def test_ipxe_shebang(self):
        self.assertTrue(self.menu.startswith("#!ipxe\n"))

    def test_menu_lists_three_boot_entries(self):
        for entry in ("ubuntu", "debian", "windows"):
            with self.subTest(entry=entry):
                self.assertRegex(self.menu, rf"(?m)^item\s+{entry}\s+")
                self.assertRegex(self.menu, rf"(?m)^:{entry}\s*$")

    def test_menu_dispatch(self):
        self.assertIn("choose target || goto start", self.menu)
        self.assertIn("goto ${target}", self.menu)

    def test_linux_entries_have_kernel_and_initrd(self):
        for entry in ("ubuntu", "debian"):
            section = re.search(
                rf"(?ms)^:{entry}\n(.*?)(?=^:[a-z]+\n|\Z)", self.menu
            )
            self.assertIsNotNone(section, f"Section {entry} absente")
            with self.subTest(entry=entry):
                self.assertIn("kernel ${boot-url}/", section.group(1))
                self.assertIn("initrd ${boot-url}/", section.group(1))
                self.assertIn("\nboot", section.group(1))

    def test_winpe_files_referenced(self):
        for filename in ("wimboot", "bcd", "boot.sdi", "boot.wim"):
            with self.subTest(filename=filename):
                self.assertIn(f"${{boot-url}}/windows/{filename}", self.menu)

    def test_server_configuration_references_menu(self):
        self.assertTrue(self.config.has_section("dhcp"))
        dhcp = self.config["dhcp"]
        self.assertEqual(dhcp.get("filename"), "ipxe.efi")
        self.assertEqual(dhcp.get("altfilename"), "menu.ipxe")
        self.assertEqual(dhcp.get("httpd"), "1")
        self.assertTrue(dhcp.get("root", "").strip())

    def test_boot_url_defined(self):
        self.assertIn("set boot-url http://${dhcp-server}", self.menu)


if __name__ == "__main__":
    unittest.main()
