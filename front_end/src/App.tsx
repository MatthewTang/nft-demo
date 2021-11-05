import React from 'react';
import logo from './logo.svg';
import './App.css';
import { ChainId, DAppProvider, useEtherBalance, useEthers } from '@usedapp/core'
import { Main } from './components/Main'
import { Header } from './components/Header';


const config = {
  supportedChains: [ChainId.Rinkeby],
  notifications: {
    expirationPeriod: 1000, // 1 second
    checkInterval: 1000 // 1 second
  }
}

function App() {
  return (
    <DAppProvider config={config}>
      <Header />
      <Main />
    </DAppProvider>
  );
}

export default App;
