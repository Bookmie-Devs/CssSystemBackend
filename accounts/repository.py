from accounts.models import CustomUser


class UserRepository:
    model = CustomUser.objects

    @classmethod
    def create_user(
        cls,
        phone,
        first_name,
        last_name,
        index_number,
        graduation_year,
        password,
    ):
        try:
            user = cls.model.create_user(
                first_name=first_name,
                last_name=last_name,
                index_number=index_number,
                graduation_year=graduation_year,
                phone=phone,
                password=password,
            )
            return user
        except CustomUser.DoesNotExist:
            return None
