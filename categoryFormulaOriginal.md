<!--- Although this is a Google Sheets formula, there is no syntax highlighting for that, so I'm marking it as java (which seems to work well). --->



Current version (with Jeremiah):



```java

={"Auto Category"&char(10)&"(based on 'Updated Initial Phrase')";ArrayFormula(if(isblank(H3:H),,(
  IFS(
    regexmatch(L3:L,"(?i)MONITOR|(?i)SENSOR|(?i)DETECTOR|(?i)PHOTOEYE|(?i)TRIGGER|TIMER|SWITCH"),"Electrical",
    regexmatch(L3:L,"(?i)SIGN|SIGN\sPANEL|(?i)LABEL|(?i)STICKER"),"Signage, Labels, and Stickers",
    regexmatch(L3:L,"(?i)LED.+LIGHT|LED.+ASSEMBL|LED.+BOARD|LED.+MODULE|LIGHT\s+BAR|LIGHT\s+BULB|LIGHT\s+FIXT"),"Lighting, Component LED's, and Light Fixtures",
    regexmatch(L3:L,"(?i)ETHERNET"),"Computer and IT",

    regexmatch(L3:L,"(?i)(CABLE|ZIP)\s+TIE"),"Mechanical Fasteners",
    regexmatch(L3:L,"^([FHPRS]H[A-Z]?[CSM]S)"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)(AXLE|CARRIAGE|U|MOUNTING)(-|\s)+BOLT"),"Mechanical Fasteners",

    regexmatch(L3:L,"(?i)CAULK|(DUCT\s+|PAINTER.+|ELECTRIC.*)TAPE"),"Sealants, Adhesives, Tape",
    regexmatch(L3:L,"(?i)HEAT\s+SHRINK|HEAT-SHRINK"),"Heat-Shrink Tubing and Sleeving",

    regexmatch(L3:L,"(?i)SPLIT\s+BOLT"),"Wire Terminals, Grounding",
    regexmatch(L3:L,"(?i)REDUCING\s+WASHER|CONDUIT"),"Cable, Hose, and Wire Management and Conduit",

    regexmatch(L3:L,"(?i)PALLET"),"Packaging and Shipping",
    regexmatch(L3:L,"(?i)(SCOTCH|CORRECTION)\s+TAPE"),"Office Supplies",
    regexmatch(L3:L,"(?i)CLAMP\s+MOUNT|DIN\s+"),"Brackets, Armatures, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)FOAM(.+RAIN|.*WATERFALL)"),"Assemblies",
    regexmatch(L3:L,"(?i)MOTOR\s+STARTER|CIRCUIT\s+BREAKER|CONTROL\sPANEL"),"Starters, Circuit Breakers, Control Panels, and Enclosures",
    regexmatch(L3:L,"(?i)MANIFOLD"),"Manifolds",
    regexmatch(L3:L,"(?i)GAUGE|METER"),"Gauges and Indicators",
    regexmatch(L3:L,"(?i)VALVE"),"Valves and Pressure Regulators",

    regexmatch(L3:L,"[Dd]rop\s[Tt]ube"),"Tanks, Reservoirs, and Drop Tubes", 
    regexmatch(L3:L,"(?i)TANK|(?i)RESERVOIR"),"Tanks, Reservoirs, and Drop Tubes",

    regexmatch(L3:L,"(?i)BUSHING|FLANGE|BEARING|ROD(\s|-)+END"),"Bushings, Flanges, Bearings, and Rod Ends",
    regexmatch(L3:L,"(?i)GROMMET|EDGE\s+TRIM"),"Grommets and Trim",
    regexmatch(L3:L,"(?i)ELBOW"),"Hose, Tube, and Pipe Fittings",

    regexmatch(L3:L,"(?i)BRACKET|(?i)ARMATURE|(?i)MOUNT|(?i)CLAMP"),"Brackets, Armatures, Mounts, and Clamps",

    regexmatch(L3:L,"(?i)ENCLOSURE|JUNCTION\s+BOX"),"Starters, Circuit Breakers, Control Panels, and Enclosures",

    regexmatch(L3:L,"(?i)Motor|(?i)PUMP|(?i)ENGINE"),"Motors and Pumps",
    regexmatch(L3:L,"(?i)SOLENOID|(?i)ACTUATOR"),"Solenoids and Actuators",
    regexmatch(L3:L,"(?i)BLOWER|(?i)FAN"),"Blowers and Fans",
    regexmatch(L3:L,"(?i)KIT"),"Kits",
    regexmatch(L3:L,"(?i)BAR|(?i)ROD|(?i)ANGLE|(?i)TUBE"),"Raw Materials and Bar Stock"
   )
  )
))}

```

Before Jeremiah

```java

={"Auto Category"&char(10)&"(based on 'Updated Initial Phrase')";ArrayFormula(if(isblank(H3:H),,(
  IFS(
    regexmatch(L3:L,"(?i)MONITOR|(?i)SENSOR|(?i)DETECTOR|(?i)PHOTOEYE|(?i)TRIGGER|TIMER|SWITCH"),"Sensors, Detectors, Photoeyes, Triggers",
    regexmatch(L3:L,"(?i)SIGN|SIGN\sPANEL|(?i)LABEL|(?i)STICKER"),"Signage, Labels, and Stickers",
    regexmatch(L3:L,"(?i)LED.+LIGHT|LED.+ASSEMBL|LED.+BOARD|LED.+MODULE|LIGHT\s+BAR|LIGHT\s+BULB|LIGHT\s+FIXT"),"Lighting, Component LED's, and Light Fixtures",
    regexmatch(L3:L,"(?i)ETHERNET"),"Computer and IT",

    regexmatch(L3:L,"(?i)(CABLE|ZIP)\s+TIE"),"Mechanical Fasteners",
    regexmatch(L3:L,"^([FHPRS]H[A-Z]?[CSM]S)"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)(AXLE|CARRIAGE|U|MOUNTING)(-|\s)+BOLT"),"Mechanical Fasteners",

    regexmatch(L3:L,"(?i)CAULK|(DUCT\s+|PAINTER.+|ELECTRIC.*)TAPE"),"Sealants, Adhesives, Tape",
    regexmatch(L3:L,"(?i)HEAT\s+SHRINK|HEAT-SHRINK"),"Heat-Shrink Tubing and Sleeving",

    regexmatch(L3:L,"(?i)SPLIT\s+BOLT"),"Wire Terminals, Grounding",
    regexmatch(L3:L,"(?i)REDUCING\s+WASHER|CONDUIT"),"Cable, Hose, and Wire Management and Conduit",

    regexmatch(L3:L,"(?i)PALLET"),"Packaging and Shipping",
    regexmatch(L3:L,"(?i)(SCOTCH|CORRECTION)\s+TAPE"),"Office Supplies",
    regexmatch(L3:L,"(?i)CLAMP\s+MOUNT|DIN\s+"),"Brackets, Armatures, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)FOAM(.+RAIN|.*WATERFALL)"),"Assemblies",
    regexmatch(L3:L,"(?i)MOTOR\s+STARTER|CIRCUIT\s+BREAKER|CONTROL\sPANEL"),"Starters, Circuit Breakers, Control Panels, and Enclosures",
    regexmatch(L3:L,"(?i)MANIFOLD"),"Manifolds",
    regexmatch(L3:L,"(?i)GAUGE|METER"),"Gauges and Indicators",
    regexmatch(L3:L,"(?i)VALVE"),"Valves and Pressure Regulators",

    regexmatch(L3:L,"[Dd]rop\s[Tt]ube"),"Tanks, Reservoirs, and Drop Tubes", 
    regexmatch(L3:L,"(?i)TANK|(?i)RESERVOIR"),"Tanks, Reservoirs, and Drop Tubes",

    regexmatch(L3:L,"(?i)BUSHING|FLANGE|BEARING|ROD(\s|-)+END"),"Bushings, Flanges, Bearings, and Rod Ends",
    regexmatch(L3:L,"(?i)GROMMET|EDGE\s+TRIM"),"Grommets and Trim",
    regexmatch(L3:L,"(?i)ELBOW"),"Hose, Tube, and Pipe Fittings",

    regexmatch(L3:L,"(?i)BRACKET|(?i)ARMATURE|(?i)MOUNT|(?i)CLAMP"),"Brackets, Armatures, Mounts, and Clamps",

    regexmatch(L3:L,"(?i)ENCLOSURE|JUNCTION\s+BOX"),"Starters, Circuit Breakers, Control Panels, and Enclosures",

    regexmatch(L3:L,"(?i)Motor|(?i)PUMP|(?i)ENGINE"),"Motors and Pumps",
    regexmatch(L3:L,"(?i)SOLENOID|(?i)ACTUATOR"),"Solenoids and Actuators",
    regexmatch(L3:L,"(?i)BLOWER|(?i)FAN"),"Blowers and Fans",
    regexmatch(L3:L,"(?i)KIT"),"Kits",
    regexmatch(L3:L,"(?i)BAR|(?i)ROD|(?i)ANGLE|(?i)TUBE"),"Raw Materials and Bar Stock"
   )
  )
))}

```
bushing, flange, shim, gasket, o-ring,

bushings, Flanges, Bearings, and Rod-ends

bumpers, grommets, and trim
10-3936


Original base formula with extra regex features.
```java 

={"Category";ArrayFormula(if(isblank(H3:H),,(
  IFS(
    regexmatch(H3:H,".*\s*(?i)BRACKET\s*.*"),"Brackets and Armatures",
    regexmatch(H3:H,"(^|\s)(?i)BAR\s*.*|(^|\s)(?i)ROD\s*.*"),"Raw Materials and Bar Stock",
    regexmatch(H3:H,".*\s*(?i)BLOWER\s*.*"),"Blowers",
    regexmatch(H3:H,".*\s*(?i)KITS?\s*.*"),"Kits",
    regexmatch(H3:H,".*\s*(?i)MONITORS?\s*.*|.*\s*(?i)SENSORS?\s*.*|.*\s*(?i)DETECTORS?\s*.*|.*\s*(?i)PHOTOEYE?\s*.*|.*\s*(?i)TRIGGERS?\s*.*"),"sensors, detectors, photoeyes, triggers"
   )
  )
))}

```
