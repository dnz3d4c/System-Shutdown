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

openedDlg = 0

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = u"System Shutdown"

	def script_dlgSystemShutdown (self, gesture):
		global openedDlg
		if openedDlg == 0:
			openedDlg = 1
			dlg = wx.TextEntryDialog(gui.mainFrame, _(u'종료 시간 입력'), _(u'시스템 종료'))
			def callback(result):
				if result == wx.ID_OK:
					global openedDlg
					openedDlg = 0
					wx.CallLater(100, self.systemShutdown, dlg.GetValue())
				elif result == wx.ID_CANCEL:
					openedDlg = 0
			gui.runScriptModalDialog(dlg, callback)
		else:
			ui.message(u"대화상자가 이미 열려잇습니다.")

	script_dlgSystemShutdown.__doc__ = _(u"시스템을 죵료합니다.")

	def systemShutdown(self, shutdownTime):
		if shutdownTime == u"":
			speech.cancelSpeech()
			ui.message(u'값을 잘못 입력하셨습니다.')
		else:
			value = int(shutdownTime)
			speech.cancelSpeech()
			ui.message(shutdownTime + u'초 후 시스템이 종료됩니다.')
			win32api.InitiateSystemShutdown("127.0.0.1", None, value, 1, 0)

	def script_cancelSystemShutdown(self, gesture):
		try:
			win32api.AbortSystemShutdown(u"127.0.0.1")
		except:
			ui.message(u"예약된 시스템 종료 작업이 없습니다.")

	script_cancelSystemShutdown.__doc__ = _(u"예약된 시스템 종료 작업을 취소합니다.")



	__gestures = {
		"kb:Control+NVDA+w":"dlgSystemShutdown",
		"kb:NVDA+Control+q":"cancelSystemShutdown"

	}
