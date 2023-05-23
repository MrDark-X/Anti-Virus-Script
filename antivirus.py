import os

VIRUS_SIGNATURES = [
    "eicar.com",  # EICAR test file
    "W97M.Downloader",  # Microsoft Word Macro virus
    "JS/CoinMiner",  # JavaScript-based cryptocurrency miner
    "Win32.Sality",  # Polymorphic file infector
    "W32.Stuxnet",  # Stuxnet worm
    "Trojan.Ransomware",  # Ransomware Trojan
    "Worm.Blaster",  # Blaster worm
    "Trojan-Downloader.Win32.Conficker",  # Conficker worm
    "W32.Mydoom",  # Mydoom worm
    "W32.Netsky",  # Netsky worm
    "Win32.Sasser",  # Sasser worm
    "Backdoor.DarkKomet",  # DarkKomet backdoor
    "Trojan-Banker.Win32.Zbot",  # Zeus/Zbot Trojan
    "W32.Ramnit",  # Ramnit worm
    "W32.Virut",  # Virut file infector
    "Exploit.PDF.EmbeddedJS",  # PDF embedded JavaScript exploit
    "W32.Bagle",  # Bagle worm
    "W32.Sober",  # Sober worm
    "Backdoor.Rbot",  # Rbot backdoor
    "W32.Almanahe",  # Almanahe worm
    "W32.Blaster.Worm",  # Blaster worm variant
    "W32.Duqu",  # Duqu Trojan
    "W32.CodeRed",  # Code Red worm
    "W32.Slammer",  # Slammer worm
    "Exploit.MS08-067",  # MS08-067 vulnerability exploit
    "W32.Sircam",  # Sircam worm
    "W32.Magistr",  # Magistr worm
    "Backdoor.Netbus",  # Netbus backdoor
    "W32.Sobig",  # Sobig worm
    "TrojanSpy.Win32.Banker",  # Banking Trojan
    "W32.Nimda",  # Nimda worm
    "Backdoor.SubSeven",  # SubSeven backdoor
    "W32.Brontok",  # Brontok worm
    "W32.Gaobot",  # Gaobot worm
    "Trojan-Downloader.JS.Agent",  # JavaScript-based downloader Trojan
    "W32.Melissa",  # Melissa virus
    "W32.Nimnul",  # Nimnul worm
    "Trojan-Downloader.W97M.Downloader",  # Microsoft Word Macro downloader Trojan
    "W32.Lovsan",  # Lovsan/MSBlaster worm
    "W32.FunLove",  # FunLove virus
    "W32.Netsky.P",  # Netsky worm variant
    "W32.MyLife",  # MyLife worm
    "Trojan-Spy.Win32.Zbot",  # Zeus/Zbot spyware Trojan
    "W32.Klez",  # Klez worm
    "W32.CIH",  # CIH/Chernobyl virus
    "W32.Rontokbro",  # Rontokbro worm
    "W32.Bagle.Z",  # Bagle worm variant
    "W32.Mimail",  # Mimail worm
    "W32.Magistr.B",  # Magistr worm variant
    "W32.Ramnit.B",  # Ramnit worm variant
    "W32.Dumaru",  # Dumaru worm
    "W32.Sality.AE",  # Sality file infector variant
    "W32.Zotob",  # Zotob worm
    "W32.Sasser.B",  # Sasser worm variant
    "W32.Nyxem",  # Nyxem/Eye-Worm worm
    "W32.Zafi",  # Zafi worm
    "W32.Gibe",  # Gibe worm
    "W32.Korgo",  # Korgo worm
    "Trojan-Downloader.VBS.Agent",  # VBS-based downloader Trojan
    "W32.Mimail.I",  # Mimail worm variant
    "W32.Gonzales",  # Gonzales worm
    "W32.Rbot.CX",  # Rbot backdoor variant
    "W32.Mydoom.AU",  # Mydoom worm variant
    "W32.Palevo",  # Palevo worm
    "Backdoor.DarkMoon",  # DarkMoon backdoor
    "W32.Bagle.AI",  # Bagle worm variant
    "W32.Sobig.F",  # Sobig worm variant
    "W32.Ramnit.C",  # Ramnit worm variant
    "W32.Slammer.D",  # Slammer worm variant
    "W32.Conficker",  # Conficker worm variant
    "W32.Storm",  # Storm worm
    "Trojan-Downloader.W32.Small",  # Small downloader Trojan
    "W32.Gammima",  # Gammima worm
    "W32.Blaster.C",  # Blaster worm variant
    "W32.Gaobot.AO",  # Gaobot worm variant
    "W32.Brontok.Q",  # Brontok worm variant
    "W32.NetSky.AA",  # Netsky worm variant
    "W32.Bagle.AK",  # Bagle worm variant
    "W32.Swen",  # Swen worm
    "W32.Bugbear",  # Bugbear worm
    "W32.Hybris",  # Hybris worm
    "W32.Sasser.D",  # Sasser worm variant
    "W32.Mydoom.B",  # Mydoom worm variant
    "W32.Polip",  # Polip worm
    "W32.SillyFDC",  # SillyFDC worm
    "W32.Sircam.B",  # Sircam worm variant
    "W32.Netsky.AC",  # Netsky worm variant
    "W32.Dref",  # Dref Trojan
    "W32.Rontokbro.H",  # Rontokbro worm variant
    "W32.Netsky.Q",  # Netsky worm variant
    "W32.Sobig.E",  # Sobig worm variant
    "W32.Ramnit.B!inf",  # Ramnit worm variant
    "W32.Sasser.E",  # Sasser worm variant
    "W32.Mydoom.D",  # Mydoom worm variant
    "W32.Bagle.AO",  # Bagle worm variant
    "W32.Gaobot.AU",  # Gaobot worm variant
    "W32.Brontok.T",  # Brontok worm variant
    "W32.NetSky.C",  # Netsky worm variant
    "W32.Mytob.C",  # Mytob worm variant
    "W32.Rontokbro.L",  # Rontokbro worm variant
    "W32.SillyFDC.B",  # SillyFDC worm variant
    "W32.Sircam.C",  # Sircam worm variant
    "W32.Netsky.T",  # Netsky worm variant
    "W32.Ramnit.B!dll",  # Ramnit worm variant
    "W32.Sobig.F!inf",  # Sobig worm variant
]

def scan_file(file_path):
    """
    Scan a file for known virus signatures and perform basic heuristics analysis.
    """
    with open(file_path, "rb") as file:
        file_content = file.read()

        # Check for known virus signatures
        for signature in VIRUS_SIGNATURES:
            if signature.encode() in file_content:
                print(f"Virus found in file: {file_path}")
                return True

        # Perform heuristics analysis
        # Add your heuristics analysis logic here
        if "eval(" in file_content.decode():
            print(f"Potentially malicious code detected in file: {file_path}")
            return True

    return False

def scan_directory(directory):
    """
    Scan all files in a directory (and its subdirectories) for known virus signatures and perform basic heuristics analysis.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

# User input for directory path
directory_path = input("Enter the directory path to scan: ")

# Verify if the directory path exists
if os.path.isdir(directory_path):
    # Call the scan_directory function with the user-provided directory path
    scan_directory(directory_path)
else:
    print("Invalid directory path.")
