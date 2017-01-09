# -*- coding: utf-8 -*-
# systemShutdown: Schedule for system shutdown

#Copyright (C) 2017 aheu

#This file is covered by the MIT License.
#See the file license.txt for more details.




import globalPluginHandler
import gui
import ui
import speech
import win32api
import wx

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = u"System Shutdown"

	def script_dlgSystemShutdown (self, gesture):
		dlg = wx.TextEntryDialog(gui.mainFrame, _(u'종료 시간 입력'), _(u'시스템 종료'))
		def callback(result):
			if result == wx.ID_OK:
				wx.CallLater(100, self.systemShutdown, dlg.GetValue())

		gui.runScriptModalDialog(dlg, callback)

	script_dlgSystemShutdown.__doc__ = _(u"시스템을 죵료합니다.")

	def systemShutdown(self, shutdownTime):
		speech.cancelSpeech()
		if shutdownTime == u"":
			ui.message(u'값을 잘못 입력하셨습니다.')
		else:
			value = int(shutdownTime)
			ui.message(shutdownTime + u'초 후 시스템이 종료됩니다.')
			win32api.InitiateSystemShutdown("127.0.0.1", None, value, 1, 0)



	__gestures = {
		"kb:Control+NVDA+w":"dlgSystemShutdown"

	}
