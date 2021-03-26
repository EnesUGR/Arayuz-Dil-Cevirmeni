class AutoUpdateCheck_Github:
	def __init__(self, userVersion, ghRepositoryName, ghUsername="EnesUGR", ghMasterName="master", ghVersionFile="version.v", permission=True):
		super(AutoUpdateCheck_Github, self).__init__()
		"""
			userVersion:str -> Uygulamanın o anki versiyonu.
                PROJENİZİN ANA DİZİNİNE VERSİON DOSYASINI OLUŞTURUN.
                Örneğin: version.v --> x.x.x
                İÇERİK YALNIZCA BÖYLE OLMALDIR. 
			ghUsername:str -> Projenizin adresindeki kullanıcı ismi.
			ghRepositoryName:str -> Projenizin adresindeki repo ismi.
			ghVersionFile:str -> Adresteki versiyonunuzun yazılı olduğu dosyanın isimi. Proje gizli olmamalıdır.
			permission:bool -> Sürüm kontrolü yapılsın mı yapılmasın mı izini.

			['isitUptoDate'] True ise sürüm günceldir değilse eskidir.
		"""

		if permission != True:
			return False

		self.userVersion = userVersion
		self.rawUrl = f"https://raw.githubusercontent.com/{ghUsername}/{ghRepositoryName}/{ghMasterName}/{ghVersionFile}"
		self.result = {"Version":self.userVersion, "Up_Version":"", "isitUptoDate":False, "error":"None"}


		self.checkVersion()


	def checkVersion(self) -> dict:
		from requests import get, exceptions

		try:
			r = get(self.rawUrl)

			if r.status_code != 200:
				self.result["error"] = f"[ERROR {str(r.status_code)}]"
				return False

			self.result["Up_Version"] = r.text.split("\n")[0]
			if self.userVersion != self.result["Up_Version"]:
				self.result["isitUptoDate"] = False
			else:
				self.result["isitUptoDate"] = True			
			return self.result


		except exceptions.ConnectionError as err:
			self.result["error"] = "ConnectionError"
			return self.result


# a = AutoUpdateCheck_Github("0.0.0","EnesUGR","deneme")
# print(a.rawUrl)
# print(a.result)
# print(a.result["isitUptoDate"])