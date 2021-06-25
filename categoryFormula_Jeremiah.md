={"Auto Category"&char(10)&"(based on 'Updated Initial Phrase')";ArrayFormula(if(isblank(H3:H),,(
  IFS(
    regexmatch(L3:L,"(?i)PROBE"),"Electrical",
    regexmatch(L3:L,"(?i)TRIGGER\s+GUN|VACUUM\s+CLEANER"),"Self-Serve",

    regexmatch(L3:L,"(?i)MONITOR|(?i)SENSOR|(?i)DETECTOR|(?i)PHOTOEYE|(?i)TRIGGER|TIMER|SWITCH|WIRE\s+NUT\b"),"Electrical",
    regexmatch(L3:L,"(?i)LABEL|STICKER|TAG"),"Labels, Tags, and Stickers",
    regexmatch(L3:L,"(?i)SIGN|SIGN\sPANEL|PAVEMENT\s+MARKER"),"Signage",
    regexmatch(L3:L,"(?i)LED\s+(LIGHT|ASSEMBL|BOARD|MODULE|END|KIT)|LIGHT\s+(BAR|BULB|FIXT)"),"Electrical",
    regexmatch(L3:L,"(?i)ETHERNET|KEYBOARD"),"Electrical",
    

    regexmatch(L3:L,"(?i)GREASE\s+FITTING"),"Grease Fittings",
    regexmatch(L3:L,"(?i)PLUMBERS\s+CLOTH"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)(CABLE|ZIP)\s+TIE"),"Mechanical Fasteners",
    regexmatch(L3:L,"^([BFHPRS]H[A-Z]?[CSM]S)"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)(AXLE|CARRIAGE|U|MOUNTING|ADJUSTMENT)(-|\s)+(BOLT|SCREW)|THUNDERSTUD|\bANCHOR\b|\bTAPCON\b"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)HEX\s+(NUT|WASHER)"),"Mechanical Fasteners",

    regexmatch(L3:L,"(?i)SCREWDRIVER|PLIER|TOOL\b|BEAKER|(DROPPER|\bSPRAY)\s+BOTTLE|TEST\s+(KIT|STRIP|PROBE)|UNIVERSAL\s+SOCKET|HANDHELD|TESTING"),"Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)(NETWORK\s+|CABLE\s+)*(TESTER|SLITTER)|WRENCH|WELDING\s+WIRE"),"Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)(CUTTING|GRINDING)\s+FLUID|ANTIFREEZE|WD\-40|WELDING\s+ROD\b"),"Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)SULFURIC\s+ACID|PHENOLPHTHALEIN"),"Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)(SANDING|POLISHING|CUT(\-|\s)+OFF)\s+(BELT|DISC|WHEEL)|EMERY\s+CLOTH|SAW\s+BLADE"),"Tools and Testing Equipment",

    regexmatch(L3:L,"(?i)CAULK|\bHAND\s+CLEANER|SEALANT|(DUCT\s+|PAINTER.+|ELECTRIC.*)TAPE|(RECEIPT|PRINT|COP[IY])(ER)?\s+PAPER|(\bRULED|\bNOTE)\s*(\bPADS?\b|PAPER)"),"Consumable Supplies",
    regexmatch(L3:L,"(?i)HEAT(\s|\-)+SHRINK|LOCTITE|LIQUID\-TITE|GREASE|SPRAY\s+PAINT|PAINT\s+REMOVER|CHEMICAL\s+ADDITIVE"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)WIRE\s+(CLOTH|FABRIC|MESH)|STRAINER|BREATHER|FILTER|VENT|VACUUM\s+BAG|INLET\s+SCREEN"),"Filtration",


    regexmatch(L3:L,"(?i)SPLIT\s+BOLT"),"Electrical",
    regexmatch(L3:L,"(?i)REDUCING\s+WASHER|CONDUIT|THERMO(METER|STAT)"),"Electrical",
    regexmatch(L3:L,"(?i)HORN\b|BUZZER"),"Electrical",
    regexmatch(L3:L,"(?i)TERMINAL\s+(BLOCK|\bEND\b|JUMPER|PLUG|PLATE)|(ANALOG|DIGITAL|AC|DC)\s+(INPUT|OUTPUT)|MODBUS|POWER\s+SUPPLY|PARTITION\s+PLATE\b"),"Electrical",

    regexmatch(L3:L,"(?i)PALLET|PIPE\s+INSULATION|PACKAGING|SHIPPING\s+BRACKET|MAILER|ENVELOPE|(CORRUGATED|CARDBOARD|FILE)\s+BOX|SHRINK(\s|\-)+WRAP|POLY\s+BAG"),"Packaging and Shipping",
    regexmatch(L3:L,"(?i)(SCOTCH|CORRECTION|TEFLON)\s+TAPE|PAPER\s+(CLIP|TOWEL)|PVC\s+CEMENT|TISSUE|NOTE|STAPLE|RUBBER\s+BAND"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)CLAMP\s+MOUNT|DIN\s+|TANK\s+SUPPORT|(SUPPORT|BACK(ING){0,1}|BASE)\s+(ARM|ANGLE|PLATE|BAR)|BRACE"),"Brackets, Armatures, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)\b(CROSS|CROSSOVER)\s*(BAR|BRACE|BEAM|MEMBER)"),"Brackets, Armatures, Mounts, and Clamps",
    
    
    regexmatch(L3:L,"(?i)MOTOR\s+STARTER|CIRCUIT\s+BREAKER|CONTROL\s+(PANEL|SYS)|OPERATOR|BUTTON|MULTIPLEX\s+CONTROL"),"Electrical",
    regexmatch(L3:L,"(?i)MANIFOLD|CROSSOVER\s+PLUMBING|PLUMBING\s+GROUP|HOSE\s+(BARB|ASSEMBLY|COUPLING|GUARD|MENDER|REDUCER)"),"Fluid Storage and Transfer",
    regexmatch(L3:L,"(?i)PIPE\s+CROSS\s+CONNECTOR|(COIL(ED)*?|\bAIR)\s+HOSE"),"Fluid Storage and Transfer",
    
    regexmatch(L3:L,"(?i)GAUGE|METER"),"Fluid Control",
    regexmatch(L3:L,"(?i)VALVE|FLOAT\s+(ARM|BALL)"),"Fluid Control",

    regexmatch(L3:L,"(?i)BRACKET|ARMATURE|MOUNT|CLAMP|GUIDE"),"Brackets, Armatures, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)DROP\s+TUBE|TANK|RESERVOIR"),"Fluid Storage and Transfer", 
    

    regexmatch(L3:L,"(?i)BUSHING|FLANGE|BEARING|ROD(\s|-)+END|\bROLLER\b|GASKET|(O\-|BACK\-UP\s+)RING|SPACER|WHEEL|CASTER|AXLE|\bOIL\s+SEAL|\bRED\.\s+BUSH"),
        "Bushings, Flanges, Bearings, Rod Ends, Spacers, and Wheels",

    regexmatch(L3:L,"(?i)SPROCKET|GEAR|SHEAVE|KEYSTOCK|\bV(\s|\-)*?BELT|KEEPER\s+SHAFT"),"Transmission (Rotary Motion)",
    
    regexmatch(L3:L,"(?i)GROMMET|EDGE\s+TRIM|(FOAM|RUBBER)\s+STRIP"),"Grommets and Trim",
    
    regexmatch(L3:L,"(?i)ELBOW"),"Fluid Storage and Transfer",

    regexmatch(L3:L,"(?i)ENCLOSURE|(JUNCTION|OUTLET)\s+BOX\b|PLC|VFD|COMPUTER|TERMINAL\s+PIN|CORD\s+GRIP|WIRE\s+DUCT|EYE\s+(EMIT|REC|TRANSMIT)"),"Electrical",
      
    regexmatch(L3:L,"(?i)MOTOR|CONTROLLER"),"Electrical",
    regexmatch(L3:L,"(?i)PUMP|BLANKING\s+PLATE\b"),"Fluid Control",
    regexmatch(L3:L,"(?i)SOLENOID|ACTUATOR|NOZZLE|(FLUID|FLOW|\bAIR|HYDRAULIC)\s+(DIST|CONTR|CYLINDER|RESERVOIR)|\bFLOAT\b"),"Fluid Control",
    regexmatch(L3:L,"(?i)INJECTOR|SPRAYER"),"Injectors, Sprayers",

    regexmatch(L3:L,"(?i)BLOWER|FAN|FUSE|RELAY|SOLDER|FLUX|CABLE|\bLED\b|HEAT\s+TAPE|HEATER"),"Electrical",
    regexmatch(L3:L,"(?i)LOOP\s+(CONTROL|STRAP)"),"Electrical",
    regexmatch(L3:L,"(?i)KIT"),"Kits",
    
    regexmatch(L3:L,"(?i)(PVC|FOAM|WATERFALL).*?TUBE|NIPPLE|\bTEE\b|COUPLING"),"Fluid Storage and Transfer",
    regexmatch(L3:L,"(?i)^HOSE$|TUBING|(FLUID|TUBE|BULKHEAD|\bPLUG\b)\s+FITTINGS?|QUICK\s+DISC|PIPE|SWIVEL\s+FLOW\s+JOINT|\bCAP\b|VICTAULIC"),"Fluid Storage and Transfer",
    regexmatch(L3:L,"(?i)ALIGNMENT\s+TAB|(WALL|RE\-FEED)\s+CLIP|GATE\s+ARM\b|HINGE\s+PIN|GUSSET\s+(PLATE|BAR\b)"),"Brackets, Armatures, Mounts, and Clamps",

    regexmatch(L3:L,"(?i)FOAM(.+RAIN|.*WATERFALL)|E\-CHAIN"),"Assemblies",
    regexmatch(L3:L,"(?i)\bBAR\b|\bROD\b|ROUND\s+STOCK|\bANGLE\b|TUBE|CHANNEL|\bALL\sTHREAD|\bSHEET\b"),"Raw Materials and Bar Stock",
    regexmatch(L3:L,"(?i)MARKER|CRAYON|PENCIL|\bPEN\b|ANTI\-SEIZE|\bGLOVE\b|\bOIL\b|(CONTACT|TOILET)\s+CLEANER|TAPE\b|LUBRICANT|\bPAINT\b|RO\s+GUARD|\bTOWELS?\b"),"Consumable Supplies",
    regexmatch(L3:L,"(?i)SPRING|RETAINER"),"Springs and Retainers",
    regexmatch(L3:L,"(?i)\bNUT\b|WASHER|\bLUG\b|EYEBOLT|\bCOTTER\s+PINS?\b|FERRULE|SET\s+SCREW"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)BALLAST|\bE(\-|\s+)STOP\b|\bKNOB\b|\bLAMP\b|CONTACT(OR|\s+BLOCK)?|INSULATED\s+WIRE|JUMPER|(SHIELDED|POWER)\s+CORD|CORDSET|\bELECTRIC(AL)?\b"),"Electrical",
    regexmatch(L3:L,"(?i)BRIDGE\s+(COVER|END)|BOLLARD|BELT\s+GUARD|SIDE\s+PLATE"),"Body Panels",
    regexmatch(L3:L,"(?i)MECHANICAL\s+ADAPTER"),"Bushings, Flanges, Bearings, Rod Ends, Spacers, and Wheels",
    regexmatch(L3:L,"(?i)CLAMSHELL|BUCKET|BRUSH"),"Self-Serve",
    regexmatch(L3:L,"(?i)BUMPER|IMPACT\s+STRIP"),"Grommets and Trim",
    regexmatch(L3:L,"(?i)COIN\s+(ACCEPTOR|DEFLECTOR)"),"Point of Sale",

    regexmatch(L3:L,"(?i)(BACK(ING)?|COVER)\s+PLATE"),"Backing and Cover Plates",

    regexmatch(L3:L,"(?i)\bKEY\b|CRANK|DRIVE\s+SHAFT"),"Transmission (Rotary Motion)",
    regexmatch(L3:L,"(?i)\b(UNI)?STRUT\b"),"Brackets, Armatures, Mounts, and Clamps",

    regexmatch(L3:L,"(?i)REPAIR|ANODIZE|(POWDER|CLEAR|EPOXY)\s+COAT|FREIGHT|MACHINING|^PACKAGING$|^ASSEMBLY$|^U\.L\.\s+APPROVED\s+ASSEMBLY$|PURCHASING|RECEIVING|POLISHING|BLASTING|SHIPPING|LOADING|TRANSPORTATION|WELDING"),
        "Labor, Processes, and Services",

    regexmatch(L3:L,"(?i)SPRAY(ER)?\s+HEAD"),"Injectors, Sprayers",

    regexmatch(L3:L,"(?i)BATCH\s+ORDER|MASTER\s+LIST"),"Batch Ordering and Master Lists"
   )
  )
))}