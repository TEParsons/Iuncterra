# Deigenic species

Deigen are creatures born from the union of two celestials within the material world. They cannot produce offspring themselves, but can breed with [sapient species](/species/sapient).

```mermaid
---
title: Pylogenic tree of the deigenic species of Iuncterra
---
flowchart LR

%% define nodes
subgraph celestials [<a href=/cosmology>Celestials</a>]
veldor([<a href=/cosmology/fey/regional_fey/veldor>Veldor</a>])
deia([<a href=/cosmology/fey/major_fey/deia>Deia</a>])
ouron([<a href=/cosmology/fey/major_fey/ouron>Ouron</a>])
jor([<a href=/cosmology/fey/fey_tira/jor>Jor</a>])
hyron([<a href=/cosmology/fey_tira/hyron>Hyron</a>])
avikath([<a href=/cosmology/daemons/malefices/avikath>Avikath</a>])
erodite([<a href=/cosmology/daemons/erodite>Erodite</a>])
hermet([<a href=/cosmology/daemons/seraphim/hermet>Hermet</a>])
loga([<a href=/cosmology/daemons/malefices/loga>Loga</a>])
lilit([<a href=/cosmology/daemons/malefices/lilit>Lilit</a>])
surt([<a href=/cosmology/daemons/malefices/surt>Surt</a>])
end
subgraph deigen [<a href=/species/deigen>Deigen</a>]
subgraph dragons[<a href=/species/deigen/dragons>Dragons</a>]
draconus><a href=/species/deigen/dragons/draconus>Draconus</a>]
kypra[<a href=/species/deigen/dragons/kypra>Kypra</a>]
end
nymph[<a href=/species/deigen/nymph>Nymph</a>]
djinn[<a href=/species/deigen/djinn>Djinn</a>]
nymph[<a href=/species/deigen/nymph>Nymph</a>]
thunderbeast><a href=/species/deigen/thunderbeast>Thunderbeast</a>]
lilitun[<a href=/species/deigen/lilitun>Lilitun</a>]
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
hyron --> pegasos
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