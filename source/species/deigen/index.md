# Deigenic species

Deigen are creatures born from the union of two celestials within the material world. They cannot produce offspring themselves, but can breed with [sapient species](/species/sapient).

```mermaid
---
title: Pylogenic tree of the deigenic species of Iuncterra
---
flowchart LR

%% define nodes
subgraph fey [<a href=/cosmology/fey>Daemons</a>]
veldor([<a href=/cosmology/fey/regional_fey/veldor>Veldor</a>])
deia([<a href=/cosmology/fey/major_fey/deia>Deia</a>])
ouron([<a href=/cosmology/fey/major_fey/ouron>Ouron</a>])
jor([[Jor](/cosmology/fey/fey_tira/jor)])
hyron([[Hyron](/cosmology/fey_tira/hyron)])
end
subgraph daemons [<a href=/cosmology/daemons>Daemons</a>]
avikath([<a href=/cosmology/daemons/malefices/avikath>Avikath</a>])
erodite([[Erodite](/cosmology/daemons/erodite)])
hermet([<a href=/cosmology/daemons/seraphim/hermet>Hermet</a>])
loga([[Loga](/cosmology/daemons/malefices/loga)])
lilit([[Lilit](/cosmology/daemons/malefices/lilit)])
surt([[Surt](/cosmology/daemons/malefices/surt)])
end
subgraph deigen [<a href=/species/deigen>Deigen</a>]
subgraph dragons[<a href=/species/deigen/dragons>Dragons</a>]
draconus><a href=/species/deigen/dragons/draconus>Draconus</a>]
kypra[<a href=/species/deigen/dragons/kypra>Kypra</a>]
end
nymph[<a href=/species/deigen/nymph>Nymph</a>]
djinn[[Djinn](/species/deigen/djinn)]
nymph[[Nymph](/species/deigen/nymph)]
thunderbeast>[Thunderbeast](/species/deigen/thunderbeast)]
lilitun[[Lilitun](/species/deigen/lilitun)]
pegasos>Pegasos]
griffon>Griffon]
end

%% define relations
avikath --> draconus
veldor --> draconus
avikath --> kypra
erodite --> nymph
deia --> nymph
loga --> djinn
deia --> thunderbeast
ouron --> thunderbeast
lilit --> lilitun
surt --> lilitun
hermet --> pegasos
hyra --> pegasos
hermet --> griffon
jor --> griffon

%% legend
subgraph legend [Legend]
  alive[Alive]
  extinct>Extinct]
  immortal([Immortal])
  
  parent[ ]
  child[ ]
  immortalparent([ ])

  alive ~~~ extinct ~~~ immortal
  immortalparent -->|descent| child
end
```