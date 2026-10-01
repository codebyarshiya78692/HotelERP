from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = (
        "Create IDDS Chef and Waiter groups and "
        "multiple operational staff accounts."
    )

    def handle(
        self,
        *args,
        **options,
    ):

        # =====================================================
        # GROUPS
        # =====================================================

        chef_group, _ = Group.objects.get_or_create(
            name="Chef",
        )

        waiter_group, _ = Group.objects.get_or_create(
            name="Waiter",
        )

        # =====================================================
        # CHEF ACCOUNTS
        # =====================================================

        chef_accounts = [
            {
                "username": "chef",
                "password": "Chef@12345",
                "first_name": "Kitchen",
                "last_name": "Chef 1",
            },
            {
                "username": "chef2",
                "password": "Chef2@12345",
                "first_name": "Kitchen",
                "last_name": "Chef 2",
            },
            {
                "username": "chef3",
                "password": "Chef3@12345",
                "first_name": "Kitchen",
                "last_name": "Chef 3",
            },
        ]

        # =====================================================
        # WAITER ACCOUNTS
        # =====================================================

        waiter_accounts = [
            {
                "username": "waiter",
                "password": "Waiter@12345",
                "first_name": "Restaurant",
                "last_name": "Waiter 1",
            },
            {
                "username": "waiter2",
                "password": "Waiter2@12345",
                "first_name": "Restaurant",
                "last_name": "Waiter 2",
            },
            {
                "username": "waiter3",
                "password": "Waiter3@12345",
                "first_name": "Restaurant",
                "last_name": "Waiter 3",
            },
        ]

        # =====================================================
        # CREATE / UPDATE CHEFS
        # =====================================================

        self.stdout.write("")

        self.stdout.write(
            self.style.SUCCESS(
                "SETTING UP CHEF ACCOUNTS"
            )
        )

        for data in chef_accounts:

            user, created = User.objects.get_or_create(
                username=data["username"],
            )

            user.set_password(
                data["password"]
            )

            user.first_name = data["first_name"]

            user.last_name = data["last_name"]

            user.is_staff = True

            user.is_active = True

            user.save()

            user.groups.add(
                chef_group
            )

            action = (
                "Created"
                if created
                else "Updated"
            )

            self.stdout.write(
                f"  {action}: {user.username}"
            )

        # =====================================================
        # CREATE / UPDATE WAITERS
        # =====================================================

        self.stdout.write("")

        self.stdout.write(
            self.style.SUCCESS(
                "SETTING UP WAITER ACCOUNTS"
            )
        )

        for data in waiter_accounts:

            user, created = User.objects.get_or_create(
                username=data["username"],
            )

            user.set_password(
                data["password"]
            )

            user.first_name = data["first_name"]

            user.last_name = data["last_name"]

            user.is_staff = True

            user.is_active = True

            user.save()

            user.groups.add(
                waiter_group
            )

            action = (
                "Created"
                if created
                else "Updated"
            )

            self.stdout.write(
                f"  {action}: {user.username}"
            )

        # =====================================================
        # DISPLAY LOGIN INFORMATION
        # =====================================================

        self.stdout.write("")

        self.stdout.write(
            self.style.SUCCESS(
                "=========================================="
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "IDDS MULTI-STAFF LOGIN READY"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "=========================================="
            )
        )

        self.stdout.write("")

        self.stdout.write(
            "CHEF ACCOUNTS:"
        )

        self.stdout.write(
            "  chef   / Chef@12345"
        )

        self.stdout.write(
            "  chef2  / Chef2@12345"
        )

        self.stdout.write(
            "  chef3  / Chef3@12345"
        )

        self.stdout.write("")

        self.stdout.write(
            "WAITER ACCOUNTS:"
        )

        self.stdout.write(
            "  waiter   / Waiter@12345"
        )

        self.stdout.write(
            "  waiter2  / Waiter2@12345"
        )

        self.stdout.write(
            "  waiter3  / Waiter3@12345"
        )

        self.stdout.write("")

        self.stdout.write(
            "All staff use:"
        )

        self.stdout.write(
            "  /accounts/login/"
        )

        self.stdout.write("")

        self.stdout.write(
            self.style.SUCCESS(
                "Each staff member has an independent account."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Orders are assigned individually after acceptance."
            )
        )

        self.stdout.write("")