class BaseStore:
    def __init__(self):
        pass

    async def set(self, key, value): ...

    async def rm(self, key): ...

    async def get(self, key): ...