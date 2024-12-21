from accounts.models import CustomUser


class UserRepository:
    model = CustomUser.objects

    @classmethod
    def create_user(cls, phone, first_name, last_name, index_number, password):
        try:
            user = cls.model.create_user(
                first_name=first_name,
                last_name=last_name,
                index_number=index_number,
                phone=phone,
                password=password,
            )
            return user
        except CustomUser.DoesNotExist:
            return None
