# import jwt
# from django.conf import settings
# from django.http import HttpResponse
#
#
# # copy的之前的项目，可以学习，暂时用不上
#
# def bc_jwt(fn):
#     def decorated_fn(*args, **kwargs):
#         request = args[1]
#
#         key = 'HTTP_X_BC_JWT'
#
#         if key not in request.META:
#             return HttpResponse('Must provide X-BC-JWT header to this endpoint', status=401)
#
#         token = request.META[key]
#
#         try:
#             claims = jwt.decode(
#                 token,
#                 settings.APP_CLIENT_SECRET,
#                 algorithms='HS512',
#                 audience=settings.APP_CLIENT_ID,
#             )
#         except Exception as e:
#             return HttpResponse('Invalid X-BC-JWT provided', status=403)
#
#         request.META['user_information'] = {
#             'customer_id': str(claims['customer']['id']),
#             'store_hash': claims['store_hash'],
#         }
#
#         return fn(*args, **kwargs)
#
#     return decorated_fn
#
#
# def http_command(fn):
#     def decorated_fn(*args, **kwargs):
#         request = args[1]
#         key = 'HTTP_X_AUTH_TOKEN'
#
#         print('request.META:', request.META)
#
#         if key not in request.META:
#             return HttpResponse('Must provide X-Auth-Token header to this endpoint', status=401)
#
#         x_store_hash_key = 'HTTP_X_STOREHASH'
#         if x_store_hash_key not in request.META:
#             return HttpResponse('Must provide X-storeHash header to this endpoint', status=401)
#
#         token = request.META[key]
#         print('token:', token)
#         stores = settings.HTTP_COMMAND_TOKEN
#         print('stores:', stores)
#
#         store_hash = request.META[x_store_hash_key]
#         source_token = str(stores.get(store_hash, None))
#
#         print('source_token:', source_token)
#         if str(token) != str(source_token):
#             return HttpResponse('Invalid token', status=403)
#
#         request.META['user_information'] = {
#             'store_hash': store_hash,
#         }
#
#         return fn(*args, **kwargs)
#
#     return decorated_fn
#
#
# def http_referer(fn):
#     def decorated_fn(*args, **kwargs):
#         request = args[1]
#         http_referer_whitelist = settings.HTTP_REFERER_WHITELIST.get('ipay88_http_referer', '')
#         print('http_referer_whitelist:', http_referer_whitelist)
#         key = 'HTTP_REFERER'
#         print('request.META:', request.META)
#         http_referer = request.META.get(key, '')
#         if http_referer is None or http_referer == '':
#             return HttpResponse('No permission to operate', status=403)
#         if str(http_referer) != str(http_referer_whitelist):
#             return HttpResponse('No permission to operate', status=403)
#         return fn(*args, **kwargs)
#
#     return decorated_fn
