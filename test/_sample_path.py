import pathlib
import winreg

class SamplePath:
    @staticmethod
    def __subkey_iterator(key):
        i = 0
        while True:
            try:
                name = winreg.EnumKey(key, i)
                yield name, winreg.OpenKey(key, name)
                i += 1
            except WindowsError as e:
                break
    
    @staticmethod
    def _find_sample_path():
        INSTALL_KEY_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        install_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, INSTALL_KEY_PATH)
        wellcads = []
        for _, key in SamplePath.__subkey_iterator(install_key):
            try:
                if winreg.QueryValueEx(key, "DisplayName")[0] == "WellCAD (x64)":
                    version = winreg.QueryValueEx(key, "Version")[0]
                    path = pathlib.Path(winreg.QueryValueEx(key, "InstallLocation")[0])
                    wellcads.append((version, path))
            except FileNotFoundError:
                pass
        wellcads.sort()
        if not wellcads:
            raise RuntimeError("Couldn't find any 64-bit versions of WellCAD installed")
        return wellcads[-1][1] / "Samples"