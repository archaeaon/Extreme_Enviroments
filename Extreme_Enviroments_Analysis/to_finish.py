def function_test_stuff():
    #############
    default_headerList = []
    default_headerList.extend(['Timestamp', 'A', 'B', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5'])
    default_headerList.extend(['B', 'C', 'D1', 'D2', 'D3', 'D4', 'D5', 'RightGauge(mBar)', 'MiddleGauge(mBar)'])
    default_headerList.extend(['LeftGauge(mBar)', 'AddedHeliumRight(mBar)', 'AddedHeliumMiddle(mBar)'])
    default_headerList.extend(['AddedHeliumLeft(mBar)', 'Cycles', 'Stage', 'Binary', 'RightCompressor'])
    default_headerList.extend(['LeftCompressor', 'TurboPump(mBar)', 'TubePressure(mBar)', 'ChamberPressure(mBar)'])
    default_headerList.extend(['CompressedAir(PSI)', 'ColdplateOutput', 'FingerOutput', 'R0:BP1', 'R1:BP1', 'R2:BP1'])
    default_headerList.extend(
        ['R4:BP1', 'R5:BP1', 'R6:BP1', 'R7:BP1', 'R8:BP1', 'R9:BP1', 'R10:BP1', 'R11:BP1', 'R12:BP1'])
    default_headerList.extend(['R13:BP1', 'R15:BP1', 'R16:BP1', 'R17:BP1', 'R18:BP1', 'R20:BP1', 'R21:BP1', 'R22:BP1'])
    default_headerList.extend(['R23:BP1', 'R24:BP1', 'R25:BP1', 'R26:BP1', 'R27:BP1', 'R28:BP1', 'R29:BP1', 'R31:BP1'])
    default_headerList.extend(['R32:BP1', 'R33:BP1', 'R34:BP1', 'R36:BP1', 'R37:BP1', 'R38:BP1', 'R39:BP1', 'R40:BP1'])
    default_headerList.extend(['R41:BP1', 'R42:BP1', 'R43:BP1', 'R44:BP1', 'R45:BP1', 'R47:BP1', 'R48:BP1', 'R49:BP1'])
    default_headerList.extend(['R50:BP1', 'R52:BP1', 'R53:BP1', 'R54:BP1', 'R55:BP1', 'R56:BP1', 'R57:BP1', 'R58:BP1'])
    default_headerList.extend(['R59:BP1', 'R60:BP1', 'R61:BP1', 'R63:BP1', 'R64:BP1', 'R65:BP1', 'R66:BP1', 'R68:BP1'])
    default_headerList.extend(['R69:BP1', 'R70:BP1', 'R71:BP1', 'R72:BP1', 'R73:BP1', 'R74:BP1', 'R75:BP1', 'R76:BP1'])
    default_headerList.extend(['R77:BP1', 'R79:BP1', 'R80:BP1', 'R81:BP1', 'R82:BP1', 'R84:BP1', 'R85:BP1', 'R86:BP1'])
    default_headerList.extend(['R87:BP1', 'R88:BP1', 'R89:BP1', 'R90:BP1', 'R91:BP1', 'R92:BP1', 'R93:BP1', 'R95:BP1'])
    default_headerList.extend(
        ['R96:BP1', 'R97:BP1', 'R98:BP1', 'R100:BP1', 'R101:BP1', 'R102:BP1', 'R103:BP1', 'R104:BP1'])
    default_headerList.extend(
        ['R105:BP1', 'R106:BP1', 'R107:BP1', 'R108:BP1', 'R109:BP1', 'R111:BP1', 'R112:BP1', 'R113:BP1'])
    default_headerList.extend(
        ['R114:BP1', 'R116:BP1', 'R117:BP1', 'R118:BP1', 'R119:BP1', 'R120:BP1', 'R121:BP1', 'R122:BP1'])
    default_headerList.extend(
        ['R123:BP1', 'R124:BP1', 'R125:BP1', 'R127:BP1', 'R128:BP1', 'R129:BP1', 'R130:BP1', 'R132:BP1'])
    default_headerList.extend(
        ['R133:BP1', 'R134:BP1', 'R135:BP1', 'R136:BP1', 'R137:BP1', 'R138:BP1', 'R139:BP1', 'R140:BP1'])
    default_headerList.extend(
        ['R141:BP1', 'R143:BP1', 'R144:BP1', 'R145:BP1', 'R146:BP1', 'R148:BP1', 'R149:BP1', 'R150:BP1'])
    default_headerList.extend(
        ['R151:BP1', 'R152:BP1', 'R153:BP1', 'R154:BP1', 'R155:BP1', 'R156:BP1', 'R157:BP1', 'R159:BP1'])
    default_headerList.extend(
        ['R160:BP1', 'R161:BP1', 'R162:BP1', 'R164:BP1', 'R165:BP1', 'R166:BP1', 'R167:BP1', 'R168:BP1'])
    default_headerList.extend(
        ['R169:BP1', 'R170:BP1', 'R171:BP1', 'R172:BP1', 'R173:BP1', 'R175:BP1', 'R176:BP1', 'R177:BP1'])
    default_headerList.extend(
        ['R178:BP1', 'R180:BP1', 'R181:BP1', 'R182:BP1', 'R183:BP1', 'R184:BP1', 'R185:BP1', 'R186:BP1'])
    default_headerList.extend(
        ['R187:BP1', 'R188:BP1', 'R189:BP1', 'R191:BP1', 'R192:BP1', 'R193:BP1', 'R194:BP1', 'R196:BP1'])
    default_headerList.extend(
        ['R197:BP1', 'R198:BP1', 'R199:BP1', 'R200:BP1', 'R201:BP1', 'R202:BP1', 'R203:BP1', 'R204:BP1'])
    default_headerList.extend(
        ['R205:BP1', 'R207:BP1', 'R208:BP1', 'R209:BP1', 'R210:BP1', 'R212:BP1', 'R213:BP1', 'R214:BP1'])
    default_headerList.extend(
        ['R215:BP1', 'R216:BP1', 'R217:BP1', 'R218:BP1', 'R219:BP1', 'R220:BP1', 'R221:BP1', 'R223:BP1'])
    default_headerList.extend(
        ['R224:BP1', 'R225:BP1', 'R226:BP1', 'R228:BP1', 'R229:BP1', 'R230:BP1', 'R231:BP1', 'R232:BP1'])
    default_headerList.extend(
        ['R233:BP1', 'R234:BP1', 'R235:BP1', 'R236:BP1', 'R237:BP1', 'R239:BP1', 'R240:BP1', 'R241:BP1'])
    default_headerList.extend(
        ['R242:BP1', 'R244:BP1', 'R245:BP1', 'R246:BP1', 'R247:BP1', 'R248:BP1', 'R249:BP1', 'R250:BP1'])
    default_headerList.extend(
        ['R251:BP1', 'R252:BP1', 'R253:BP1', 'R255:BP1', 'R336:BP1', 'R337:BP1', 'R338:BP1', 'R340:BP1'])
    default_headerList.extend(
        ['R341:BP1', 'R342:BP1', 'R343:BP1', 'R344:BP1', 'R345:BP1', 'R346:BP1', 'R347:BP1', 'R348:BP1'])
    default_headerList.extend(['R349:BP1', 'R351:BP1'])

    default_headerList.extend(
        ['R0:BP2', 'R1:BP2', 'R2:BP2', 'R4:BP2', 'R5:BP2', 'R6:BP2', 'R7:BP2', 'R8:BP2', 'R9:BP2', 'R10:BP2'])
    default_headerList.extend(
        ['R11:BP2', 'R12:BP2', 'R13:BP2', 'R15:BP2', 'R16:BP2', 'R17:BP2', 'R18:BP2', 'R20:BP2', 'R21:BP2'])
    default_headerList.extend(
        ['R22:BP2', 'R23:BP2', 'R24:BP2', 'R25:BP2', 'R26:BP2', 'R27:BP2', 'R28:BP2', 'R29:BP2', 'R31:BP2'])
    default_headerList.extend(
        ['R32:BP2', 'R33:BP2', 'R34:BP2', 'R36:BP2', 'R37:BP2', 'R38:BP2', 'R39:BP2', 'R40:BP2', 'R41:BP2'])
    default_headerList.extend(
        ['R42:BP2', 'R43:BP2', 'R44:BP2', 'R45:BP2', 'R47:BP2', 'R48:BP2', 'R49:BP2', 'R50:BP2', 'R52:BP2'])
    default_headerList.extend(
        ['R53:BP2', 'R54:BP2', 'R55:BP2', 'R56:BP2', 'R57:BP2', 'R58:BP2', 'R59:BP2', 'R60:BP2', 'R61:BP2'])
    default_headerList.extend(
        ['R63:BP2', 'R64:BP2', 'R65:BP2', 'R66:BP2', 'R68:BP2', 'R69:BP2', 'R70:BP2', 'R71:BP2', 'R72:BP2'])
    default_headerList.extend(
        ['R73:BP2', 'R74:BP2', 'R75:BP2', 'R76:BP2', 'R77:BP2', 'R79:BP2', 'R80:BP2', 'R81:BP2', 'R82:BP2'])
    default_headerList.extend(
        ['R84:BP2', 'R85:BP2', 'R86:BP2', 'R87:BP2', 'R88:BP2', 'R89:BP2', 'R90:BP2', 'R91:BP2', 'R92:BP2'])
    default_headerList.extend(
        ['R93:BP2', 'R95:BP2', 'R96:BP2', 'R97:BP2', 'R98:BP2', 'R100:BP2', 'R101:BP2', 'R102:BP2', 'R103:BP2'])
    default_headerList.extend(
        ['R104:BP2', 'R105:BP2', 'R106:BP2', 'R107:BP2', 'R108:BP2', 'R109:BP2', 'R111:BP2', 'R112:BP2'])
    default_headerList.extend(
        ['R113:BP2', 'R114:BP2', 'R116:BP2', 'R117:BP2', 'R118:BP2', 'R119:BP2', 'R120:BP2', 'R121:BP2'])
    default_headerList.extend(
        ['R122:BP2', 'R123:BP2', 'R124:BP2', 'R125:BP2', 'R127:BP2', 'R128:BP2', 'R129:BP2', 'R130:BP2'])
    default_headerList.extend(
        ['R132:BP2', 'R133:BP2', 'R134:BP2', 'R135:BP2', 'R136:BP2', 'R137:BP2', 'R138:BP2', 'R139:BP2'])
    default_headerList.extend(
        ['R140:BP2', 'R141:BP2', 'R143:BP2', 'R144:BP2', 'R145:BP2', 'R146:BP2', 'R148:BP2', 'R149:BP2'])
    default_headerList.extend(
        ['R150:BP2', 'R151:BP2', 'R152:BP2', 'R153:BP2', 'R154:BP2', 'R155:BP2', 'R156:BP2', 'R157:BP2'])
    default_headerList.extend(
        ['R159:BP2', 'R160:BP2', 'R161:BP2', 'R162:BP2', 'R164:BP2', 'R165:BP2', 'R166:BP2', 'R167:BP2'])
    default_headerList.extend(
        ['R168:BP2', 'R169:BP2', 'R170:BP2', 'R171:BP2', 'R172:BP2', 'R173:BP2', 'R175:BP2', 'R176:BP2'])
    default_headerList.extend(
        ['R177:BP2', 'R178:BP2', 'R180:BP2', 'R181:BP2', 'R182:BP2', 'R183:BP2', 'R184:BP2', 'R185:BP2'])
    default_headerList.extend(
        ['R186:BP2', 'R187:BP2', 'R188:BP2', 'R189:BP2', 'R191:BP2', 'R192:BP2', 'R193:BP2', 'R194:BP2'])
    default_headerList.extend(
        ['R196:BP2', 'R197:BP2', 'R198:BP2', 'R199:BP2', 'R200:BP2', 'R201:BP2', 'R202:BP2', 'R203:BP2'])
    default_headerList.extend(
        ['R204:BP2', 'R205:BP2', 'R207:BP2', 'R208:BP2', 'R209:BP2', 'R210:BP2', 'R212:BP2', 'R213:BP2'])
    default_headerList.extend(
        ['R214:BP2', 'R215:BP2', 'R216:BP2', 'R217:BP2', 'R218:BP2', 'R219:BP2', 'R220:BP2', 'R221:BP2'])
    default_headerList.extend(
        ['R223:BP2', 'R224:BP2', 'R225:BP2', 'R226:BP2', 'R228:BP2', 'R229:BP2', 'R230:BP2', 'R231:BP2'])
    default_headerList.extend(
        ['R232:BP2', 'R233:BP2', 'R234:BP2', 'R235:BP2', 'R236:BP2', 'R237:BP2', 'R239:BP2', 'R240:BP2'])
    default_headerList.extend(
        ['R241:BP2', 'R242:BP2', 'R244:BP2', 'R245:BP2', 'R246:BP2', 'R247:BP2', 'R248:BP2', 'R249:BP2'])
    default_headerList.extend(
        ['R250:BP2', 'R251:BP2', 'R252:BP2', 'R253:BP2', 'R255:BP2', 'R320:BP2', 'R321:BP2', 'R322:BP2'])
    default_headerList.extend(
        ['R324:BP2', 'R325:BP2', 'R326:BP2', 'R327:BP2', 'R328:BP2', 'R329:BP2', 'R330:BP2', 'R331:BP2'])
    default_headerList.extend(
        ['R332:BP2', 'R333:BP2', 'R335:BP2', 'R336:BP2', 'R337:BP2', 'R338:BP2', 'R340:BP2', 'R341:BP2'])
    default_headerList.extend(
        ['R342:BP2', 'R343:BP2', 'R344:BP2', 'R345:BP2', 'R346:BP2', 'R347:BP2', 'R348:BP2', 'R349:BP2'])
    default_headerList.extend(['R351:BP2'])

    default_headerList.extend(
        ['C3:BP1', 'C14:BP1', 'C19:BP1', 'C30:BP1', 'C35:BP1', 'C46:BP1', 'C51:BP1', 'C62:BP1', 'C67:BP1'])
    default_headerList.extend(
        ['C78:BP1', 'C83:BP1', 'C94:BP1', 'C99:BP1', 'C110:BP1', 'C115:BP1', 'C126:BP1', 'C131:BP1'])
    default_headerList.extend(
        ['C142:BP1', 'C147:BP1', 'C158:BP1', 'C163:BP1', 'C174:BP1', 'C179:BP1', 'C190:BP1', 'C195:BP1'])
    default_headerList.extend(['C206:BP1', 'C211:BP1', 'C222:BP1', 'C227:BP1', 'C238:BP1', 'C243:BP1', 'C254:BP1'])

    default_headerList.extend(
        ['C256:BP1', 'C257:BP1', 'C258:BP1', 'C259:BP1', 'C260:BP1', 'C261:BP1', 'C262:BP1', 'C263:BP1'])
    default_headerList.extend(
        ['C264:BP1', 'C265:BP1', 'C266:BP1', 'C267:BP1', 'C268:BP1', 'C269:BP1', 'C270:BP1', 'C271:BP1'])
    default_headerList.extend(
        ['C272:BP1', 'C273:BP1', 'C274:BP1', 'C275:BP1', 'C276:BP1', 'C277:BP1', 'C278:BP1', 'C279:BP1'])
    default_headerList.extend(
        ['C280:BP1', 'C281:BP1', 'C282:BP1', 'C283:BP1', 'C284:BP1', 'C285:BP1', 'C286:BP1', 'C287:BP1'])

    default_headerList.extend(['C339:BP1', 'C350:BP1'])

    default_headerList.extend(
        ['C3:BP2', 'C14:BP2', 'C19:BP2', 'C30:BP2', 'C35:BP2', 'C46:BP2', 'C51:BP2', 'C62:BP2', 'C67:BP2'])
    default_headerList.extend(
        ['C78:BP2', 'C83:BP2', 'C94:BP2', 'C99:BP2', 'C110:BP2', 'C115:BP2', 'C126:BP2', 'C131:BP2'])
    default_headerList.extend(
        ['C142:BP2', 'C147:BP2', 'C158:BP2', 'C163:BP2', 'C174:BP2', 'C179:BP2', 'C190:BP2', 'C195:BP2'])
    default_headerList.extend(['C206:BP2', 'C211:BP2', 'C222:BP2', 'C227:BP2', 'C238:BP2', 'C243:BP2', 'C254:BP2'])

    default_headerList.extend(
        ['C288:BP2', 'C289:BP2', 'C290:BP2', 'C291:BP2', 'C292:BP2', 'C293:BP2', 'C294:BP2', 'C295:BP2'])
    default_headerList.extend(
        ['C296:BP2', 'C297:BP2', 'C298:BP2', 'C299:BP2', 'C300:BP2', 'C301:BP2', 'C302:BP2', 'C303:BP2'])
    default_headerList.extend(
        ['C304:BP2', 'C305:BP2', 'C306:BP2', 'C307:BP2', 'C308:BP2', 'C309:BP2', 'C310:BP2', 'C311:BP2'])
    default_headerList.extend(
        ['C312:BP2', 'C313:BP2', 'C314:BP2', 'C315:BP2', 'C316:BP2', 'C317:BP2', 'C318:BP2', 'C319:BP2'])

    default_headerList.extend(['C323:BP2', 'C334:BP2', 'C339:BP2', 'C350:BP2'])

    default_headerList.extend(['R0:MUX', 'R1:MUX', 'R2:MUX', 'R3:MUX', 'R4:MUX', 'R5:MUX', 'R6:MUX', 'R7:MUX'])
    default_headerList.extend(['R8:MUX', 'R9:MUX', 'R10:MUX', 'R11:MUX', 'R12:MUX', 'R13:MUX', 'R14:MUX', 'R15:MUX'])
    default_headerList.extend(['R16:MUX', 'R17:MUX', 'R18:MUX', 'R19:MUX', 'R20:MUX', 'R21:MUX', 'R22:MUX', 'R23:MUX'])
    default_headerList.extend(['R24:MUX', 'R25:MUX', 'R26:MUX', 'R27:MUX', 'R28:MUX', 'R29:MUX', 'R30:MUX', 'R31:MUX'])
    default_headerList.extend(['R32:MUX', 'R33:MUX', 'R34:MUX', 'R35:MUX', 'R36:MUX', 'R37:MUX', 'R38:MUX', 'R39:MUX'])
    default_headerList.extend(['R40:MUX', 'R41:MUX', 'R42:MUX', 'R43:MUX', 'R44:MUX', 'R45:MUX', 'R46:MUX', 'R47:MUX'])
    default_headerList.extend(['R48:MUX', 'R49:MUX', 'R50:MUX', 'R51:MUX', 'R52:MUX', 'R53:MUX', 'R54:MUX', 'R55:MUX'])
    default_headerList.extend(['R56:MUX', 'R57:MUX', 'R58:MUX', 'R59:MUX', 'R60:MUX', 'R61:MUX', 'R62:MUX', 'R63:MUX'])
    default_headerList.extend(['R64:MUX', 'R65:MUX', 'R66:MUX', 'R67:MUX', 'R68:MUX', 'R69:MUX', 'R70:MUX', 'R71:MUX'])
    default_headerList.extend(['R72:MUX', 'R73:MUX', 'R74:MUX', 'R75:MUX', 'R76:MUX', 'R77:MUX', 'R78:MUX', 'R79:MUX'])
    default_headerList.extend(['R80:MUX', 'R81:MUX', 'R82:MUX', 'R83:MUX', 'R84:MUX', 'R85:MUX', 'R86:MUX', 'R87:MUX'])
    default_headerList.extend(['R88:MUX', 'R89:MUX', 'R90:MUX', 'R91:MUX', 'R92:MUX', 'R93:MUX', 'R94:MUX', 'R95:MUX'])
    default_headerList.extend(
        ['R96:MUX', 'R97:MUX', 'R98:MUX', 'R99:MUX', 'R100:MUX', 'R101:MUX', 'R102:MUX', 'R103:MUX'])
    default_headerList.extend(
        ['R104:MUX', 'R105:MUX', 'R106:MUX', 'R107:MUX', 'R108:MUX', 'R109:MUX', 'R110:MUX', 'R111:MUX'])
    default_headerList.extend(
        ['R112:MUX', 'R113:MUX', 'R114:MUX', 'R115:MUX', 'R116:MUX', 'R117:MUX', 'R118:MUX', 'R119:MUX'])
    default_headerList.extend(
        ['R120:MUX', 'R121:MUX', 'R122:MUX', 'R123:MUX', 'R124:MUX', 'R125:MUX', 'R126:MUX', 'R127:MUX'])
    default_headerList.extend(
        ['R128:MUX', 'R129:MUX', 'R130:MUX', 'R131:MUX', 'R132:MUX', 'R133:MUX', 'R134:MUX', 'R135:MUX'])
    default_headerList.extend(
        ['R136:MUX', 'R137:MUX', 'R138:MUX', 'R139:MUX', 'R140:MUX', 'R141:MUX', 'R142:MUX', 'R143:MUX'])
    default_headerList.extend(
        ['R144:MUX', 'R145:MUX', 'R146:MUX', 'R147:MUX', 'R148:MUX', 'R149:MUX', 'R150:MUX', 'R151:MUX'])
    default_headerList.extend(
        ['R152:MUX', 'R153:MUX', 'R154:MUX', 'R155:MUX', 'R156:MUX', 'R157:MUX', 'R158:MUX', 'R159:MUX'])

    print(default_headerList)

###############################
###############################
###############################
