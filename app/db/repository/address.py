from app.db.models.model import Address
from app.db.repository.base import BaseRepository


class AddressRepository(BaseRepository[Address]):
    pass


address_repository = AddressRepository(Address)
