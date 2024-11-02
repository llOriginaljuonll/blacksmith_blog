from django.db import models

class Blog(models.Model):
    """
    Options:
        auto_now อัปเดตข้อมูลอัตโนมัติ ทุกครั้งที่มีการแก้ไขข้อมูล
    """
    name = models.CharField(max_length=100)
    body = models.TextField()
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        # verbose_name = "บทความ"
        verbose_name_plural = "Blog"

    def __str__(self):
        return f"No.{self.id} {self.name}"
    