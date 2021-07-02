={"Auto Category"&char(10)&"(based on 'Updated Initial Phrase')";ArrayFormula(if(isblank(H3:H),,(
  IFS(
    regexmatch(L3:L,"(?i)PROBE"),"Electrical",
    regexmatch(L3:L,"(?i)TRIGGER\s+GUN|VACUUM\s+CLEANER|WAND"),"Self-Serve",

    regexmatch(L3:L,"(?i)\bHYDRA\-CANNON|HYDRADAPTER|HYDROMINDER|FLOAT\s+SWITCH|\b(WICK|SHAFT\s+PROTECTOR)\b"),"Fluid Control",
    regexmatch(L3:L,"(?i)MONITOR|SENSOR|DETECTOR|PHOTO(\-|\s+)?EYE|TRIGGER|TRANSDUCER|TIMER|SWITCH|WIRE\s+NUT\b|\bBUS\s*?BAR\b"),"Electrical",
    regexmatch(L3:L,"(?i)LABEL|STICKER|TAG"),"Labels, Tags, and Stickers",
    regexmatch(L3:L,"(?i)SIGN|SIGN\sPANEL|PAVEMENT\s+MARKER"),"Signage",
    regexmatch(L3:L,"(?i)LED\s+(LIGHT|ASSEMBL|BOARD|MODULE|END|KIT)|LIGHT\s+(BAR|BULB|FIXT)|THERMO(METER|STAT)"),"Electrical",
    regexmatch(L3:L,"(?i)ETHERNET|KEYBOARD|MEMORY\s+CARD"),"Electrical",

    regexmatch(L3:L,"(?i)(PUMP\s+STATION|TROLLEY)\s+FRAME|\bUPRIGHT\b"),"Structural Frames and Linkages",
    
    regexmatch(L3:L,"(?i)GREASE\s+FITTINGS?|LUBRICATORS?|OILERS?"),"McDonald's Fries",
    regexmatch(L3:L,"(?i)PLUMBERS\s+CLOTH"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)(CABLE|ZIP)\s+TIE\s+PLATE"),"Brackets, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)(CABLE|ZIP)\s+TIE|SPIRAL\s+BUNDLING\s+WRAP|LANYARD"),"Mechanical Fasteners",

    regexmatch(L3:L,"^([BFHPRS]H[A-Z]?[CSM]S)"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)(AXLE|CARRIAGE|U|MOUNTING|ADJUSTMENT)(-|\s)+(BOLT|SCREW)|THUNDERSTUD|\bANCHOR\b|\bTAPCON\b|\bCLEVIS\b|\bSNAP\s+RINGS?\b"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)HEX\s+(NUT|WASHER)|S\-HOOK|\bSTRAP\b"),"Mechanical Fasteners",

    regexmatch(L3:L,"(?i)SCREWDRIVER|PLIER|TOOL\b|BEAKER|(DROPPER|\bSPRAY)\s+BOTTLE|TEST\s+(KIT|STRIP|PROBE)|UNIVERSAL\s+SOCKET|HANDHELD|TESTING|\bHAND\s+PUMPS?\b|HANDLE|\bHOLDER\b"),
        "Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)WRENCH|WELDING\s+WIRE|FUNNEL|SOLDER|FLUX|(NETWORK\s+|CABLE\s+)*(TESTER|SLITTER)|CHAIN\s+PULLER"),"Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)(CUTTING|GRINDING)\s+FLUID|ANTIFREEZE|WD\-40|WELDING\s+ROD\b"),"Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)SULFURIC\s+ACID|PHENOLPHTHALEIN"),"Tools and Testing Equipment",
    regexmatch(L3:L,"(?i)(SANDING|POLISHING|CUT(\-|\s)+OFF)\s+(BELT|DISC|WHEEL)|EMERY\s+CLOTH|SAW\s+BLADE"),"Tools and Testing Equipment",

    regexmatch(L3:L,"(?i)CAULK|\bHAND\s+CLEANER|SEALANT|(DUCT\s+|PAINTER.+|ELECTRIC.*)TAPE|(RECEIPT|PRINT|COP[IY])(ER)?\s+PAPER|(\bRULED|\bNOTE)\s*(\bPADS?\b|PAPER)"),"Consumable Supplies",
    regexmatch(L3:L,"(?i)HEAT(\s|\-)+SHRINK|LOCTITE|LIQUID\-TITE|GREASE|SPRAY\s+PAINT|PAINT\s+REMOVER|CHEMICAL\s+ADDITIVE"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)WIRE\s+(CLOTH|FABRIC|MESH)|STRAINER|BREATHER|FILTER|\bVENT\b|VACUUM\s+BAG|INLET\s+SCREEN|\bR\.O\.\s+(MEMBRANE|HOUSING|SYSTEM)"),"Filtration",

    regexmatch(L3:L,"(?i)SPLIT\s+BOLT|REDUCING\s+WASHER"),"Electrical",
    regexmatch(L3:L,"(?i)CONDUIT|CORD\s+GRIP|WIRE\s+DUCT|HOSE\s+(SLEEV(E|ING)|PROTECTOR|SHEATH(ING)?)|E\-CHAIN\s+.*?SEPARATOR"),"Cable and Hose Management 36",
    regexmatch(L3:L,"(?i)HORN\b|BUZZER"),"Electrical",
    regexmatch(L3:L,"(?i)TERMINAL\s+(BLOCK|\bEND\b|JUMPER|PLUG|PLATE)|(ANALOG|DIGITAL|AC|DC)\s+(INPUT|OUTPUT)|MODBUS|POWER\s+SUPPLY|PARTITION\s+PLATE\b"),"Electrical",

    regexmatch(L3:L,"(?i)PALLET|PIPE\s+INSULATION|PACKAGING|SHIPPING\s+BRACKET|MAILER|ENVELOPE|(CORRUGATED|CARDBOARD|FILE)\s+BOX|SHRINK(\s|\-)+WRAP|POLY\s+BAG"),"Packaging and Shipping",
    regexmatch(L3:L,"(?i)(SCOTCH|CORRECTION|TEFLON)\s+TAPE|PAPER\s+(CLIP|TOWEL)|PVC\s+CEMENT|TISSUE|NOTE|STAPLE|RUBBER\s+BAND"),"Consumable Supplies",

    regexmatch(L3:L,"(?i)CLAMP\s+MOUNT|DIN\s+|TANK\s+SUPPORT|(SUPPORT|BACK(ING){0,1}|BASE)\s+(ARM|ANGLE|BAR|PLATE)|BRACE"),"Brackets, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)\b(CROSS|CROSSOVER)\s*(BAR|BRACE|BEAM|MEMBER)"),"Brackets, Mounts, and Clamps",
    
    regexmatch(L3:L,"(?i)MOTOR\s+STARTER|CIRCUIT\s+BREAKER|CONTROL\s+(PANEL|SYS|BOARD)|OPERATOR|BUTTON|MULTIPLEX\s+CONTROL"),"Electrical",
    
    regexmatch(L3:L,"(?i)MANIFOLD\s+VALVE|FLOAT\s+(ARM|BALL)|VALVE|GAUGE|METER|INDICATOR"),"Fluid Control",
    
    regexmatch(L3:L,"(?i)MANIFOLD|PORT\s+BLOCK|CROSSOVER\s+PLUMBING|PLUMBING\s+GROUP|HOSE\s+(BARB|ASSEMBLY|COUPLING|GUARD|MENDER|REDUCER)"),"Fluid Storage and Transfer",
    regexmatch(L3:L,"(?i)PIPE\s+CROSS\s+CONNECTOR|ELBOW|(COIL(ED)*?|\bAIR)\s+HOSE"),"Fluid Storage and Transfer",
    

    regexmatch(L3:L,"(?i)BRACKET|ARMATURE|MOUNT|CLAMP|GUIDE|BEARING\s+SUPPORT"),"Brackets, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)DROP\s+TUBE|TANK|RESERVOIR"),"Fluid Storage and Transfer", 
    
    regexmatch(L3:L,"(?i)(ROUND|ACCURACY|BEARING\s+SHAFT|THREADED)\s+ROD\b|(RECTANGULAR|HEX(AGONAL)?)\s+BAR\s+STOCK"),"Raw Materials and Bar Stock",

    regexmatch(L3:L,"(?i)BUSHING|FLANGE|BEARING|\bROLLER\b|GASKET|(O\-|BACK\-UP\s+)RING|SPACER|\bOIL\s+SEAL|\bRED\.\s+BUSH"),
        "Bushings, Flanges, Bearings, Spacers, and Wheels",

    regexmatch(L3:L,"(?i)SPROCKET|GEAR|SHEAVE|KEYSTOCK|THRUST\s+WASHER|\bV(\s|\-)*?BELT|(KEEPER|ROTAT(E|ION))\s+SHAFT|(SHAFT|MECHANICAL)\s+ADAPTER|WHEEL|CASTER|AXLE|\bBELT\s+ADJUST"),"Transmission (Rotary Motion)",
    
    regexmatch(L3:L,"(?i)GROMMET|BUMPER|EDGE\s+TRIM|(FOAM|RUBBER|IMPACT)\s+STRIP|CRUTCH\s+TIPS?\b"),"Grommets and Trim",

    regexmatch(L3:L,"(?i)ENCLOSURE|(JUNCTION|OUTLET)\s+BOX\b|PLC|VFD|COMPUTER|TERMINAL\s+PIN|EYE\s+(EMIT|REC|TRANSMIT)|PHOTO(\-|\s+)?EYE\s+HOUSING"),"Electrical",
      
    regexmatch(L3:L,"(?i)MOTOR|STARTER|CONTROL(LER|\s+UNIT)|POWER\s+DISTRIBUTION\s+BLOCK|POWER\s+REGULATOR"),"Electrical",
    regexmatch(L3:L,"(?i)PUMP|BLANKING\s+PLATE\b|REGULATOR|\bFDM\b"),"Fluid Control",

    regexmatch(L3:L,"(?i)SOLENOID|ACTUATOR|PULSATION\s+DAMPEN|(FLUID|FLOW|\bAIR|HYDRAULIC)\s+(DIST|CONTR|CYLINDER|RESERVOIR)|\bFLOAT\b|EXHAUST\s+MUFFLER"),"Fluid Control",
    regexmatch(L3:L,"(?i)INJECTOR|SPRAYER|AIRKNI(F|V)ES?"),"Injectors, Sprayers, and Nozzles",

    regexmatch(L3:L,"(?i)BLOWER|FAN|FUSE|RELAY|CABLE|\bLED\b|HEAT\s+TAPE|HEATER|SERVO\s+DRIVE"),"Electrical",
    regexmatch(L3:L,"(?i)LOOP\s+CONTROL|(BURIAL|SAW(\-|\s)+CUT)\s+LOOP|BEAM\s+DEFLECTOR"),"Electrical",
    regexmatch(L3:L,"(?i)\bKITS?\b"),"Kits",
    

    regexmatch(L3:L,"(?i)(BACK(ING)?|COVER)\s+PLATE|SUPPORT\s+DISC\b|ENTRANCE\s+(COVER\s+)?MAT"),"Backing and Cover Plates",

    regexmatch(L3:L,"(?i)(PVC|FOAM|WATERFALL).*?TUBE|NIPPLE|\bTEE\b|COUPLING"),"Fluid Storage and Transfer",
    regexmatch(L3:L,"(?i)^HOSE$|TUBING|(FLUID|TUBE|BULKHEAD|\bPLUG\b)\s+FITTINGS?|QUICK\s+DISC|PIPE|SWIVEL\s+FLOW\s+JOINT|\bCAP\b|VICTAULIC"),"Fluid Storage and Transfer",
    regexmatch(L3:L,"(?i)ALIGNMENT\s+TAB|(WALL|RE\-FEED)\s+CLIP|GATE\s+ARM\b|GUSSET\s+(PLATE|BAR\b)|SUPPORT\s+COLLAR"),"Brackets, Mounts, and Clamps",

    regexmatch(L3:L,"(?i)^CHAIN(\s+SET)?$"),"Mechanical Fasteners 87",

    regexmatch(L3:L,"(?i)ROUND\s+STOCK|\bANGLE\b|TUBE|CHANNEL|\bALL\sTHREAD|\bSHEET\b"),"Raw Materials and Bar Stock",

    regexmatch(L3:L,"(?i)MARKER|CRAYON|PENCIL|\bPEN\b|ANTI\-SEIZE|\bGLOVE\b|\bOIL\b|(CONTACT|TOILET)\s+CLEANER|TAPE\b|LUBRICANT|\bPAINT\b|RO\s+GUARD|\bTOWELS?\b"),"Consumable Supplies",
    regexmatch(L3:L,"(?i)SPRING|RETAINER"),"Springs and Retainers",
    regexmatch(L3:L,"(?i)\bNUT\b|WASHER|\bLUG\b|EYEBOLT|\bCOTTER\s+PINS?\b|FERRULE|SET\s+SCREW|(SHEAR|PIVOT)\s+(BOLTS?|PINS?\b|NUTS?\b)"),"Mechanical Fasteners",
    regexmatch(L3:L,"(?i)BALLAST|\bE(\-|\s+)STOP\b|\bKNOB\b|\bLAMP\b|CONTACT(OR|\s+BLOCK)?|INSULATED\s+WIRE|JUMPER|(SHIELDED|POWER)\s+CORD|CORDSET|\bELECTRIC(AL)?\b"),"Electrical",
    regexmatch(L3:L,"(?i)BRIDGE\s+(COVER|END)|BOLLARD|BELT\s+GUARD|COVER\s+PANEL|SIDE\s+PLATE|COVER\s+SUPPORT\s+DISC"),"Body Panels",

    regexmatch(L3:L,"(?i)ROD(\s|-)+END|CONNECTING\s+ROD|KNUCKLE|LINKAGE\s+ARM|TORQUE\s+ARM|TENSION\s+CYLINDER|TOP\s+BEAM|(BRIDGE|MAIN)\s+RAIL|\b(SEX|BARREL)\s+BOLT|(DRIVE|PIVOT|HINGE)\s+PIN"),
        "Structural Frames and Linkages",

    regexmatch(L3:L,"(?i)\bSHIM\b|\bSEAL\b"),"Bushings, Flanges, Bearings, Spacers, and Wheels",

    regexmatch(L3:L,"(?i)CLAMSHELL|BUCKET|BRUSH|SELF(\s|\-)+SERV"),"Self-Serve",
    
    regexmatch(L3:L,"(?i)COIN\s+(ACCEPTOR|DEFLECTOR)|\bSLUG(\s+)?BUSTER|MENU\s+STATION"),"Point of Sale",
    regexmatch(L3:L,"(?i)\bKEY\b|CRANK|(DRIVE|\bSTUB\b)\s+SHAFT"),"Transmission (Rotary Motion)",

    regexmatch(L3:L,"(?i)\b(UNI)?STRUT\b|COVER\s+SUPPORT|GUSSET"),"Brackets, Mounts, and Clamps",
    regexmatch(L3:L,"(?i)\b(LEG|FRAME)\b|(\bWELD|SHEAR|SUPPORT|\bT)(\s|\-)+PLATE\b"), "Structural Frames and Linkages",

    regexmatch(L3:L,"(?i)(\bSPLICE|PHOTO\-EYE)\s+PLATE\b"),"Plates with Strategic Holes",

    regexmatch(L3:L,"(?i)REPAIR|ANODIZE|(POWDER|CLEAR|EPOXY)\s+COAT|FREIGHT|MACHINING|^PACKAGING$|^ASSEMBLY$|^U\.L\.\s+APPROVED\s+ASSEMBLY$|PURCHASING|RECEIVING|POLISHING|BLASTING|SHIPPING|LOADING|TRANSPORTATION|WELDING"),
        "Labor, Processes, and Services",

    regexmatch(L3:L,"(?i)\b(ARM|BEAM|BOOM|SUPPORT)\b"), "Structural Frames and Linkages",

    regexmatch(L3:L,"(?i)SPRAY(ER)?\s+(HEAD|BAR)\b|NOZZLE|INJECTOR"),"Injectors, Sprayers, and Nozzles",
    regexmatch(L3:L,"(?i)\b(PLATE|LUMBER)\b"),"Raw Materials and Bar Stock",
    regexmatch(L3:L,"(?i)\bUPS\b|(I\/O\s+END|SERIAL\s+INTERFACE)\s+MODULE|\bSERVO\b"),"Electrical",
    regexmatch(L3:L,"(?i)\bHMI\b|\bSCADA\b"),"Electrical",

    regexmatch(L3:L,"(?i)\bCONVEYOR\b"),"Conveyor-specific Stuff",

    regexmatch(L3:L,"(?i)APPLICATOR\s+SET|COMPLETE\s+MACHINE|\bARCH\b|RP\s+SYSTEM|TRIPLE\s+FOAM|FOAM(.+RAIN|.*WATERFALL)|E\-CHAIN|LIGHTED\s+COVER\s+GROUP|ASSEMBLY|WELDMENT"),
        "Assemblies (Catch-all)",

    regexmatch(L3:L,"(?i)BATCH\s+ORDER|(MASTER|PARTS)\s+LIST|\bBATCH\b|VAN\s+INVENTORY"),"Batch Ordering and Master Lists",
    regexmatch(L3:L,"(?i)OPTIONS|PARTS\s+(ROOM|UNIQUE)|PETIT\s+(IN\s+HOUSE|PARTS|SUPPLIED)|REPLACEMENT\s+PL\b|PURCHASE\s+PARTS"),"Batch Ordering and Master Lists"
   )
  )
))}