# Generated from DHSemanticGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DHSemanticGrammarParser import DHSemanticGrammarParser
else:
    from DHSemanticGrammarParser import DHSemanticGrammarParser

from sensors import SensorPresence, SensorRain, SensorLight, SensorTemperature, SensorTime, SensorSmoke, SensorWind, SensorIntruders, SensorFlood, SensorGas
from Action import Action
from Transition import Transition
from behaviour import Behaviour
from State import State
from House import House
from Room import Room


# This class defines a complete listener for a parse tree produced by DHSemanticGrammarParser.
class DHSemanticGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by DHSemanticGrammarParser#casa.
    def enterCasa(self, ctx:DHSemanticGrammarParser.CasaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#casa.
    def exitCasa(self, ctx:DHSemanticGrammarParser.CasaContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#lh.
    def enterLh(self, ctx:DHSemanticGrammarParser.LhContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#lh.
    def exitLh(self, ctx:DHSemanticGrammarParser.LhContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#h.
    def enterH(self, ctx:DHSemanticGrammarParser.HContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#h.
    def exitH(self, ctx:DHSemanticGrammarParser.HContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#lp.
    def enterLp(self, ctx:DHSemanticGrammarParser.LpContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#lp.
    def exitLp(self, ctx:DHSemanticGrammarParser.LpContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#p.
    def enterP(self, ctx:DHSemanticGrammarParser.PContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#p.
    def exitP(self, ctx:DHSemanticGrammarParser.PContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#l2id.
    def enterL2id(self, ctx:DHSemanticGrammarParser.L2idContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#l2id.
    def exitL2id(self, ctx:DHSemanticGrammarParser.L2idContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#c.
    def enterC(self, ctx:DHSemanticGrammarParser.CContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#c.
    def exitC(self, ctx:DHSemanticGrammarParser.CContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#lest.
    def enterLest(self, ctx:DHSemanticGrammarParser.LestContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#lest.
    def exitLest(self, ctx:DHSemanticGrammarParser.LestContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#lactions.
    def enterLactions(self, ctx:DHSemanticGrammarParser.LactionsContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#lactions.
    def exitLactions(self, ctx:DHSemanticGrammarParser.LactionsContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#action.
    def enterAction(self, ctx:DHSemanticGrammarParser.ActionContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#action.
    def exitAction(self, ctx:DHSemanticGrammarParser.ActionContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#init.
    def enterInit(self, ctx:DHSemanticGrammarParser.InitContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#init.
    def exitInit(self, ctx:DHSemanticGrammarParser.InitContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#trans.
    def enterTrans(self, ctx:DHSemanticGrammarParser.TransContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#trans.
    def exitTrans(self, ctx:DHSemanticGrammarParser.TransContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#t.
    def enterT(self, ctx:DHSemanticGrammarParser.TContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#t.
    def exitT(self, ctx:DHSemanticGrammarParser.TContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#lsl.
    def enterLsl(self, ctx:DHSemanticGrammarParser.LslContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#lsl.
    def exitLsl(self, ctx:DHSemanticGrammarParser.LslContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#lal.
    def enterLal(self, ctx:DHSemanticGrammarParser.LalContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#lal.
    def exitLal(self, ctx:DHSemanticGrammarParser.LalContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#lsg.
    def enterLsg(self, ctx:DHSemanticGrammarParser.LsgContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#lsg.
    def exitLsg(self, ctx:DHSemanticGrammarParser.LsgContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#lag.
    def enterLag(self, ctx:DHSemanticGrammarParser.LagContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#lag.
    def exitLag(self, ctx:DHSemanticGrammarParser.LagContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#s.
    def enterS(self, ctx:DHSemanticGrammarParser.SContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#s.
    def exitS(self, ctx:DHSemanticGrammarParser.SContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#a.
    def enterA(self, ctx:DHSemanticGrammarParser.AContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#a.
    def exitA(self, ctx:DHSemanticGrammarParser.AContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#spresencia.
    def enterSpresencia(self, ctx:DHSemanticGrammarParser.SpresenciaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#spresencia.
    def exitSpresencia(self, ctx:DHSemanticGrammarParser.SpresenciaContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#slluvia.
    def enterSlluvia(self, ctx:DHSemanticGrammarParser.SlluviaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#slluvia.
    def exitSlluvia(self, ctx:DHSemanticGrammarParser.SlluviaContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#shumo.
    def enterShumo(self, ctx:DHSemanticGrammarParser.ShumoContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#shumo.
    def exitShumo(self, ctx:DHSemanticGrammarParser.ShumoContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#sintrusos.
    def enterSintrusos(self, ctx:DHSemanticGrammarParser.SintrusosContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#sintrusos.
    def exitSintrusos(self, ctx:DHSemanticGrammarParser.SintrusosContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#sinundacion.
    def enterSinundacion(self, ctx:DHSemanticGrammarParser.SinundacionContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#sinundacion.
    def exitSinundacion(self, ctx:DHSemanticGrammarParser.SinundacionContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#sgas.
    def enterSgas(self, ctx:DHSemanticGrammarParser.SgasContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#sgas.
    def exitSgas(self, ctx:DHSemanticGrammarParser.SgasContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#siluminacion.
    def enterSiluminacion(self, ctx:DHSemanticGrammarParser.SiluminacionContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#siluminacion.
    def exitSiluminacion(self, ctx:DHSemanticGrammarParser.SiluminacionContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#stemperatura.
    def enterStemperatura(self, ctx:DHSemanticGrammarParser.StemperaturaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#stemperatura.
    def exitStemperatura(self, ctx:DHSemanticGrammarParser.StemperaturaContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#sviento.
    def enterSviento(self, ctx:DHSemanticGrammarParser.SvientoContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#sviento.
    def exitSviento(self, ctx:DHSemanticGrammarParser.SvientoContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#sreloj.
    def enterSreloj(self, ctx:DHSemanticGrammarParser.SrelojContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#sreloj.
    def exitSreloj(self, ctx:DHSemanticGrammarParser.SrelojContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#apuerta.
    def enterApuerta(self, ctx:DHSemanticGrammarParser.ApuertaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#apuerta.
    def exitApuerta(self, ctx:DHSemanticGrammarParser.ApuertaContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#acalefaccion.
    def enterAcalefaccion(self, ctx:DHSemanticGrammarParser.AcalefaccionContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#acalefaccion.
    def exitAcalefaccion(self, ctx:DHSemanticGrammarParser.AcalefaccionContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#apersiana.
    def enterApersiana(self, ctx:DHSemanticGrammarParser.ApersianaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#apersiana.
    def exitApersiana(self, ctx:DHSemanticGrammarParser.ApersianaContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#aluz.
    def enterAluz(self, ctx:DHSemanticGrammarParser.AluzContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#aluz.
    def exitAluz(self, ctx:DHSemanticGrammarParser.AluzContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#aventana.
    def enterAventana(self, ctx:DHSemanticGrammarParser.AventanaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#aventana.
    def exitAventana(self, ctx:DHSemanticGrammarParser.AventanaContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#afrio.
    def enterAfrio(self, ctx:DHSemanticGrammarParser.AfrioContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#afrio.
    def exitAfrio(self, ctx:DHSemanticGrammarParser.AfrioContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#agas.
    def enterAgas(self, ctx:DHSemanticGrammarParser.AgasContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#agas.
    def exitAgas(self, ctx:DHSemanticGrammarParser.AgasContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#atoldo.
    def enterAtoldo(self, ctx:DHSemanticGrammarParser.AtoldoContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#atoldo.
    def exitAtoldo(self, ctx:DHSemanticGrammarParser.AtoldoContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#aalarma.
    def enterAalarma(self, ctx:DHSemanticGrammarParser.AalarmaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#aalarma.
    def exitAalarma(self, ctx:DHSemanticGrammarParser.AalarmaContext):
        pass


    # Enter a parse tree produced by DHSemanticGrammarParser#aemergencia.
    def enterAemergencia(self, ctx:DHSemanticGrammarParser.AemergenciaContext):
        pass

    # Exit a parse tree produced by DHSemanticGrammarParser#aemergencia.
    def exitAemergencia(self, ctx:DHSemanticGrammarParser.AemergenciaContext):
        pass



del DHSemanticGrammarParser