from app.database.sql.models.model import Address
from app.database.sql.repository.base import BaseRepository


class AddressRepository(BaseRepository[Address]):
    pass


address_repository = AddressRepository(Address)
