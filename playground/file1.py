import playground.user as user
from playground.classUser import User

result = user.getEntryByUser('frithjof')
print(result.getName())
print(result.getNumber())
print(result)

# fred = User('frithjof','25102000')
# user.addUser(fred)