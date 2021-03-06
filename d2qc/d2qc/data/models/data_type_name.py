from django.contrib.gis.db import models

class DataTypeName(models.Model):
    class Meta:
        db_table = 'd2qc_data_type_names'
        unique_together = ('name', 'is_reference')

    id = models.AutoField(primary_key=True)
    data_type = models.ForeignKey(
        'DataType',
        related_name = 'data_type_names',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )
    name = models.CharField(max_length=255)
    is_reference = models.BooleanField(default=False)
    operation_type = models.ForeignKey(
        'OperationType',
        related_name = 'data_type_names',
        on_delete = models.PROTECT,
        blank = True,
        null = True,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def get_normalization_name(self):
        return f"NORM#{self.name}"
