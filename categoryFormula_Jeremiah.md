<!--- Although this is a Google Sheets formula, there is no syntax highlighting for that, so I'm marking it as java (which seems to work well). --->



Current version (with Jeremiah):


```java

={"Auto Category"&char(10)&"(based on 'Updated Initial Phrase')";ArrayFormula(if(isblank(H3:H),,(
  IFS(
    regexmatch(L3:L,"(?i)PROBE"),"Electrical",
    regexmatch(L3:L,"(?i)TRIGGER\s+GUN|VACUUM\s+CLEANER"),"Self-Serve",

    regexmatch(L3:L,"(?i)MONITOR|(?i)SENSOR|(?i)DETECTOR|(?i)PHOTOEYE|(?i)TRIGGER|TIMER|SWITCH"),"Electrical",
    regexmatch(L3:L,"(?i)LABEL|STICKER|TAG"),"Labels, Tags, and Stickers",
    regexmatch(L3:L,"(?i)SIGN|SIGN\sPANEL|PAVEMENT\s+MARKER"),"Signage",
    regexmatch(L3:L,"(?i)LED\s+(LIGHT|ASSEMBL|BOARD|MODULE|END)|LIGHT\s+(BAR|BULB|FIXT)"),"Electrical",
    regexmatch(L3:L,"(?i)ETHERNET"),"Electrical",

    regexmatch(L3:L,"(?i)GREASE\s+FITTING"),"Grease Fittings",
    regexmatch(L3:L,"(?i)GREASE|(CUTTING|GRINDING)\s+FLUID|SPRAY\s+PAINT|ANTIFREEZE"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)(CABLE|ZIP)\s+TIE"),"Mechanical Fasteners",
    regexmatch(L3:L,"^([BFHPRS]H[A-Z]?[CSM]S)"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)(AXLE|CARRIAGE|U|MOUNTING|ADJUSTMENT)(-|\s)+(BOLT|SCREW)|THUNDERSTUD"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)HEX\s+(NUT|WASHER)"),"Mechanical Fasteners",

    regexmatch(L3:L,"(?i)SCREWDRIVER|PLIER|TOOL\b|BEAKER|TEST\s+(KIT|STRIP|PROBE)|UNIVERSAL\s+SOCKET|HANDHELD|TESTING|CUT(\-|\s)OFF\s+WHEEL"),"Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)(NETWORK\s+|CABLE\s+)*(TESTER|SLITTER)|WRENCH"),"Tools and Testing Equipment",

    regexmatch(L3:L,"(?i)CAULK|\bHAND\s+CLEANER|SEALANT|(DUCT\s+|PAINTER.+|ELECTRIC.*)TAPE|(RECEIPT|PRINT|COP[IY])(ER)?\s+PAPER"),"Consumable Supplies",
    regexmatch(L3:L,"(?i)HEAT\s+SHRINK|HEAT-SHRINK|LOCTITE|LIQUID\-TITE|FLUX"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)WIRE\s+(CLOTH|FABRIC|MESH)|STRAINER|FILTER|VENT|VACUUM\s+BAG|INLET\s+SCREEN"),"Filtration",


    regexmatch(L3:L,"(?i)SPLIT\s+BOLT"),"Electrical",
    regexmatch(L3:L,"(?i)REDUCING\s+WASHER|CONDUIT|THERMO(METER|STAT)"),"Electrical",
    regexmatch(L3:L,"(?i)TERMINAL\s+BLOCK|(ANALOG|DIGITAL|AC|DC)\s+(INPUT|OUTPUT)|MODBUS|POWER\s+SUPPLY"),"Electrical",

    regexmatch(L3:L,"(?i)PALLET|PIPE\s+INSULATION|PACKAGING|SHIPPING\s+BRACKET|MAILER|ENVELOPE|CORRUGATED\s+CARDBOARD\s+BOX"),"Packaging and Shipping",
    regexmatch(L3:L,"(?i)(SCOTCH|CORRECTION|TEFLON)\s+TAPE|PAPER\s+(CLIP|TOWEL)|PVC\s+CEMENT|TISSUE|SANDING\s+BELT|NOTE"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)CLAMP\s+MOUNT|DIN\s+|TANK\s+SUPPORT|(SUPPORT|BACK(ING){0,1}|BASE)\s+(ARM|ANGLE|PLATE|BAR)|BRACE"),"Brackets, Armatures, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)\b(CROSS|CROSSOVER)\s*(BAR|BRACE|BEAM|MEMBER)"),"Brackets, Armatures, Mounts, and Clamps",
    
    
    regexmatch(L3:L,"(?i)MOTOR\s+STARTER|CIRCUIT\s+BREAKER|CONTROL\s+(PANEL|SYS)|OPERATOR|BUTTON|MULTIPLEX\s+CONTROL"),"Electrical",
    regexmatch(L3:L,"(?i)MANIFOLD|CROSSOVER\s+PLUMBING|PLUMBING\s+GROUP|HOSE\s+(BARB|ASSEMBLY|COUPLING|GUARD|MENDER|REDUCER)"),"Fluid Transfer",
    regexmatch(L3:L,"(?i)PIPE\s+CROSS\s+CONNECTOR"),"Fluid Transfer",
    
    regexmatch(L3:L,"(?i)GAUGE|METER"),"Fluid Control",
    regexmatch(L3:L,"(?i)VALVE"),"Fluid Control",

    regexmatch(L3:L,"(?i)BRACKET|ARMATURE|MOUNT|CLAMP|GUIDE"),"Brackets, Armatures, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)DROP\s+TUBE|TANK|RESERVOIR"),"Fluid Transfer", 
    

    regexmatch(L3:L,"(?i)BUSHING|FLANGE|BEARING|ROD(\s|-)+END|\bROLLER\b|GASKET|(O\-|BACK\-UP\s+)RING|SPACER|WHEEL|CASTER|AXLE|\bOIL\s+SEAL|\bRED\.\s+BUSH"),"Bushings, Flanges, Bearings, Rod Ends, Spacers, and Wheels",

    regexmatch(L3:L,"(?i)SPROCKET|GEAR|SHEAVE|KEYSTOCK"),"Transmission (Rotary Motion)",
    
    regexmatch(L3:L,"(?i)GROMMET|EDGE\s+TRIM|(FOAM|RUBBER)\s+STRIP"),"Grommets and Trim",
    
    regexmatch(L3:L,"(?i)ELBOW"),"Fluid Transfer",

    regexmatch(L3:L,"(?i)ENCLOSURE|(JUNCTION|OUTLET)\s+BOX\b|PLC|VFD|COMPUTER|TERMINAL\s+PIN|CORD\s+GRIP|WIRE\s+DUCT|EYE\s+(EMIT|REC|TRANSMIT)"),"Electrical",
      
    regexmatch(L3:L,"(?i)MOTOR|CONTROLLER"),"Electrical",
    regexmatch(L3:L,"(?i)PUMP"),"Fluid Control",
    regexmatch(L3:L,"(?i)SOLENOID|ACTUATOR|NOZZLE|(FLUID|FLOW|\bAIR|HYDRAULIC)\s+(DIST|CONTR|CYLINDER)"),"Fluid Control",
    regexmatch(L3:L,"(?i)INJECTOR|SPRAYER"),"Injectors, Sprayers",

    regexmatch(L3:L,"(?i)BLOWER|FAN|FUSE|RELAY|SOLDER|CABLE|\bLED\b"),"Electrical",
    regexmatch(L3:L,"(?i)KIT"),"Kits",
    
    regexmatch(L3:L,"(?i)(PVC|FOAM|WATERFALL).*?TUBE|NIPPLE|\bTEE\b|COUPLING"),"Fluid Transfer",
    regexmatch(L3:L,"(?i)^HOSE$|TUBING|(FLUID|TUBE|BULKHEAD)\s+FITTINGS?|QUICK\s+DISC|PIPE|SWIVEL\s+FLOW\s+JOINT|\bCAP\b|VICTAULIC"),"Fluid Transfer",
    regexmatch(L3:L,"(?i)ALIGNMENT\s+TAB"),"Brackets, Armatures, Mounts, and Clamps",

    regexmatch(L3:L,"(?i)FOAM(.+RAIN|.*WATERFALL)|E\-CHAIN"),"Assemblies",
    regexmatch(L3:L,"(?i)BAR|ROD|ROUND\s+STOCK|ANGLE|TUBE|CHANNEL|\bALL\sTHREAD"),"Raw Materials and Bar Stock",
    regexmatch(L3:L,"(?i)MARKER|CRAYON|PENCIL|\bPEN\b|ANTI\-SEIZE|\bGLOVE\b|\bOIL\b"),"Consumable Supplies",
    regexmatch(L3:L,"(?i)SPRING|RETAINER"),"Springs and Retainers",
    regexmatch(L3:L,"(?i)NUT|WASHER|LUG|EYEBOLT"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)BALLAST|\bE\s+STOP\b|\bKNOB\b|\bLAMP\b"),"Electrical",
    regexmatch(L3:L,"(?i)BRIDGE\s(COVER|END\s(PLATE|STOP))"),"Body Panels",
    regexmatch(L3:L,"(?i)MECHANICAL\s+ADAPTER"),"Bushings, Flanges, Bearings, Rod Ends, Spacers, and Wheels",
    

    regexmatch(L3:L,"(?i)BATCH\s+ORDER|MASTER\s+LIST"),"Batch Ordering and Master Lists"
   )
  )
))}

```

