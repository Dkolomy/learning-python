import time

# def causeError():
#   start = time.time()
#   try:
#     time.sleep(0.5)
#     return 1 / 0
#   except TypeError as e:
#     print(f"Type Error: {e}")
#   except ZeroDivisionError as e:
#     print(f"Zero Division Error: {e}")
#   except ValueError as e:
#     print(f"ValueError: {e}")
#   except NameError as e:
#     print(f"Name Error: {e}")
#   except AttributeError as e:
#     print(f"Attribute Error: {e}")
#   except IndexError as e:
#     print(f"Index Error: {e}")
#   except Exception as e:
#     print(f"Error: {e}")
#   finally:
#     end = time.time()
#     print(f"Time taken: {end - start} seconds")

# causeError()

# Custom Decorator
# def handleException(func):
#   def wrapper(*args):
#     try:
#       func(*args)
#     except TypeError as e:
#       print(f"Type Error: {e}")
#     except ZeroDivisionError as e:
#       print(f"Zero Division Error: {e}")
#     except ValueError as e:
#       print(f"ValueError: {e}")
#     except NameError as e:
#       print(f"Name Error: {e}")
#     except AttributeError as e:
#       print(f"Attribute Error: {e}")
#     except IndexError as e:
#       print(f"Index Error: {e}")
#     except Exception as e:
#       print(f"Error: {e}")
#   return wrapper

# @handleException
# def causeError():
#   return 1 / 0

# causeError()

# @handleException
# def raiseError():
#   raise ValueError("This is a test error")

# raiseError()

# Custom Exception
# class CustomException(Exception):
#   pass

# def causeCustomException():
#   raise CustomException("This is a test custom error")

# causeCustomException()

# Adding Attributes to Custom Exception
class HttpException(Exception):
  statusCode = None
  message = None

  def __init__(self):
    super().__init__(f"HTTP Error {self.statusCode}: {self.message}")

class NotFoundException(HttpException):
  statusCode = 404
  message = "Not Found"

class BadRequestException(HttpException):
  statusCode = 400
  message = "Bad Request"

class InternalServerErrorException(HttpException):
  statusCode = 500
  message = "Internal Server Error"

raise NotFoundException()