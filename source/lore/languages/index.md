# Languages

The graph below shows how the various languages of Iuncterra inherit from one another, all stemming from a single common language spoken by the first iotun.

<div class=full-width>
```mermaid
---
title: Pylogenic Tree of the Languages of Iuncterra
---
flowchart LR

%% define nodes
tunnic[Tunnic]
unthic[Unthic]
garic[Garic]
ataithan([Ataithan])
proto-dracean[Proto-Dracean]
proto-savonic[Proto-Savonic]
yamn[Yamn]
parbati([Parbati])
old-nasruki[Old Nasruki]
high-nasruki[High Nasruki]
low-nasruki([Low Nasruki])
loxan([Loxan])
uttic([Uttic])
jotic([Jotic])
atkani([Atkani])
jotun-atkani([Jotun-Atkani])
noordic([Noordic])
salean[Salean]
servian([Servian])
kypritic([Kypritic])
high-dracean([High Dracean])
low-dracean([Low Dracean])
tabax([Tabax])
scutian([Scutian])
high-savonic([High Savonic])
low-savonic([Low Savonic])
old-kushite[Old Kushite]
high-kushite([High Kushite])
low-kushite([Low Kushite])
nasruki-kushite(Nasruki Kushite)
common([Common])

%% define relations
tunnic --> unthic

unthic --> jotic
unthic --> uttic
unthic --> yamn
low-dracean -.-> noordic
uttic --> noordic
yamn --> atkani
yamn --> jotun-atkani
jotic -.-> jotun-atkani

tunnic --> garic

garic --> proto-dracean
proto-dracean --> salean
salean --> servian
salean --> kypritic
proto-dracean --> high-dracean
high-dracean --> low-dracean
servian -.-> low-dracean

garic --> proto-savonic
proto-savonic --> high-savonic
proto-savonic --> low-savonic

proto-savonic --> old-kushite
old-kushite --> high-kushite
old-kushite --> low-kushite
old-kushite -.-> nasruki-kushite

garic --> parbati
parbati --> scutian
salean -.-> scutian
parbati --> tabax
parbati --> old-nasruki
old-nasruki --> high-nasruki
old-nasruki --> low-nasruki
high-nasruki --> nasruki-kushite
low-nasruki --> loxan

garic --> ataithan

low-dracean --> common
low-savonic -.-> common
noordic -.-> common
low-kushite -.-> common
scutian -.-> common

%% legend
subgraph legend [Legend]
  extinct[Extinct]
  court(Formal Only)
  living([Living])
  parent([ ])
  child([ ])

  extinct ~~~ court ~~~ living ~~~ parent
  parent -->|descent| child
  parent -.->|influence| child
end

```
</div>