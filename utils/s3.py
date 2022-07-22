# import os
# from uuid import uuid1
#
# from django.utils.text import slugify
# from storages.backends.s3boto3 import S3Boto3Storage
# from django.conf import settings
#
#
# class S3Boto3StoragePublic(S3Boto3Storage):
#     def __init__(self, bucket=None, **settings):
#         self.querystring_auth = False
#         super(S3Boto3StoragePublic, self).__init__(acl='public-read', bucket=bucket, **settings)
#
#
# def upload_generic(folder, sub_folder, filename):
#     path = os.path.join(
#         "__debug__" if settings.DEBUG else "",
#         folder[:10],
#         sub_folder[:20],
#         f"{uuid1()}"[:20],
#         filename
#     )
#     return path
#
#
# def upload_to(instance, filename):
#     return upload_generic(instance.__class__.__name__.lower(), slugify(instance), filename)
