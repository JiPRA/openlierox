/*
 *  DedicatedControl.h
 *  OpenLieroX
 *
 *  Created by Albert Zeyer on 11.01.08.
 *  code under LGPL
 *
 */

#ifndef __DEDICATEDCONTROL_H__
#define __DEDICATEDCONTROL_H__

#include <string>

struct DedIntern;
class CWorm;
struct CmdLineIntf;

class DedicatedControl {
private:
	DedicatedControl(); ~DedicatedControl();
	bool Init_priv();
public:
	DedIntern* internData;
	
	static bool Init(); static void Uninit();
	static DedicatedControl* Get();
	
	void LobbyStarted_Signal();
	void BackToServerLobby_Signal();
	void BackToClientLobby_Signal();
	void GameLoopStart_Signal();
	void GameLoopEnd_Signal();
	void NewWorm_Signal(CWorm* w);
	void WormLeft_Signal(CWorm* w);
	void WeaponSelections_Signal();
	void GameStarted_Signal();
	void Connecting_Signal(const std::string& addr);
	void ChatMessage_Signal(CWorm* w, const std::string& message);
	void PrivateMessage_Signal(CWorm* w, CWorm* to, const std::string& message);
	void WormDied_Signal(CWorm* died, CWorm* killer);
	void WormSpawned_Signal(CWorm* worm);
	void WormGotAdmin_Signal(CWorm* worm);
	void WormAuthorized_Signal(CWorm* worm);
	
	void Menu_Frame();
	void GameLoop_Frame();
	void ChangeScript(const std::string& filename);
	bool GetNextSignal(CmdLineIntf* sender); // false means that we should not finalizeReturn() yet!
};



#endif
