from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "orders",
            "0002_staff_assignments",
        ),
        migrations.swappable_dependency(
            settings.AUTH_USER_MODEL,
        ),
    ]

    operations = [

        migrations.AddField(
            model_name="order",
            name="assigned_waiter",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={
                    "groups__name": "Waiter",
                },
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="assigned_food_orders",
                to=settings.AUTH_USER_MODEL,
            ),
        ),

    ]