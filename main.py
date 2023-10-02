from foo import Foo
from bar import Bar


aFoo = Foo(Bar("Gudule"))
print(aFoo.getBar().getName())

anotherFoo = Foo(aFoo.getBar())
print(anotherFoo.getBar().getName())

aFoo.setBar(Bar("Barnabé"))
print(anotherFoo.getBar().getName())
print(aFoo.getBar().getName())