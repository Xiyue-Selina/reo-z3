from reo import *

c1 = Connector()
c1.connect('Sync'     , 'A', 'D')
c1.connect('Sync'     , 'D', 'D1')
c1.connect('Sync'     , 'B', 'E')
c1.connect('Sync'     , 'E', 'E1')
c1.connect('Merger'   , 'D1', 'E1', 'C')
c1.connect('SyncDrain', 'E', 'G')
c1.connect('SyncDrain', 'D', 'H')
c1.connect('Fifo1e(1)'   , 'F', 'G')
c1.connect('Fifo1'    , 'G', 'H')
c1.connect('Sync'     , 'H', 'F')

c2 = Connector()
c2.connect('Sync'     , 'A', 'D')
c2.connect('LossySync'     , 'D', 'D1')
c2.connect('Sync'     , 'B', 'E')
c2.connect('LossySync'     , 'E', 'E1')
c2.connect('Merger'   , 'D1', 'E1', 'C')
c2.connect('SyncDrain', 'E', 'G')
c2.connect('SyncDrain', 'D', 'H')
c2.connect('Fifo1e(1)'   , 'F', 'G')
c2.connect('Fifo1'    , 'G', 'H')
c2.connect('Sync'     , 'H', 'F')

result1, counterexample1, smt1 = c2.isRefinementOf(c1, 10)
result2, counterexample2, smt2 = c1.isRefinementOf(c2, 10)

print(result1)
print(result2)

print(counterexample1)
print(counterexample2)