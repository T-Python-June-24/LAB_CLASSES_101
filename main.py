from panda import Panda

panda1 = Panda(name="Simon", age=10, weight=101, habitat="Forest")
panda2 = Panda(name="Patrick", age=7, weight=91, habitat="Zoo")
panda3 = Panda(name="Bob", age=5, weight=95, habitat="Sanctuary")
panda4 = Panda(name="Ross", age=21, weight=105, habitat="Mountain")

pandas = [panda1, panda2, panda3, panda4]

for panda in pandas:
    print(panda)
    print(panda.eat("bamboo"))
    print(panda.sleep(10))
    print() 