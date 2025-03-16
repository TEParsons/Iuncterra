# Sapient species

Iuncterra is home to a wide variety of sapient creatures, the graph below shows the phylogenic relationships between them.

```mermaid
---
title: Pylogenic tree of the species of Iuncterra
---
flowchart LR

%% define nodes
subgraph celestials [<a href=/cosmology>Celestials</a>]
ouron([<a href=/cosmology/fey/major_fey/ouron>Ouron</a>])
deia([<a href=/cosmology/fey/major_fey/deia>Deia</a>])
veldor([<a href=/cosmology/fey/regional_fey/veldor>Veldor</a>])
hermet([<a href=/cosmology/daemons/seraphim/hermet>Hermet</a>])
ludon([<a href=/cosmology/daemons/seraphim/ludon>Ludon</a>])
avikath([<a href=/cosmology/daemons/malefices/avikath>Avikath</a>])
zukothoth([<a href=/cosmology/daemons/malefices/zukothoth>Zukothoth</a>])
end
subgraph deigen [<a href=/species/deigen>Deigen</a>]
draconus[<a href=/species/deigen/dragons/draconus>Draconus</a>]
nymph[<a href=/species/deigen/nymph>Nymph</a>]
end
subgraph sapients [Sapient species]
iotun><a href=/species/sapient/iotun>Iotun</a>]
jotun[<a href=/species/sapient/jotun>Jotun</a>]
aarakocra[<a href=/species/sapient/aarakocra>Aarakocra</a>]
dragonborn[<a href=/species/sapient/dragonborn>Dragonborn</a>]
dwarf[<a href=/species/sapient/dwarf>Dwarf</a>]
elf[<a href=/species/sapient/elf>Elf</a>]
halfling[<a href=/species/sapient/halfling>Halfling</a>]
human[<a href=/species/sapient/human>Human</a>]
loxodon[<a href=/species/sapient/loxodon>Loxodon</a>]
orc[<a href=/species/sapient/orc>Orc</a>]
tabaxi[<a href=/species/sapient/tabaxi>Tabaxi</a>]
gandrite[<a href=/species/sapient/gandrite>Gandrite</a>]
satyr[<a href=/species/sapient/satyr>Satyr</a>]
end

%% define relations
iotun --> jotun
iotun --> dwarf
iotun --> human
iotun --> orc
iotun --> dragonborn

jotun --> gandrite

human --> elf
human --> aarakocra
human --> halfling
human --> tabaxi
human --> loxodon
human --> satyr

avikath --> draconus
veldor --> draconus
ludon --> nymph
deia --> nymph

draconus --> dragonborn
nymph --> elf

ouron -.-> loxodon
deia -.-> tabaxi
hermet -.-> aarakocra
ludon -.-> satyr
zukothoth -.-> gandrite

%% legend
subgraph legend [Legend]
  alive[Alive]
  extinct>Extinct]
  immortal([Immortal])
  
  parent[ ]
  child[ ]
  immortalparent([ ])

  alive ~~~ extinct ~~~ immortal
  parent -->|descent| child
  immortalparent -.->|interference| child
end

```

#### Ageing
Different species age at different rates. Taking the rate of ageing in humans as a baseline, equivalent ages of other species can be calculated by the following multipliers:

|/species/sapient/aging.xlsx:Multipliers|

When parents of two different species have a child, the results can vary when it comes to ageing. Generally a child of a long lived species with a shorter lived species will gain only a slight increase to their lifespan, particular when elven genes are concerned. The genes for short lifespans are generally dominant.