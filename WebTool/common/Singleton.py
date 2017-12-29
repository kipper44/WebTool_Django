class SingletonInstance:
	__instance = None

	@classmethod
	def getinstance(cls):
		return cls.__instance

	@classmethod
	def instance(cls, *args, **kargs):
		cls.__instance = cls(*args, **kargs)
		cls.instance = cls.getinstance
		return cls.__instance