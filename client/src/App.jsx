import { useState } from 'react'
import './App.css'
import TextBlock from './components/TextBlock'
import NewsIcon from './components/NewsIcon'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className='App'>
        <TextBlock type="main-summary"/>
        <TextBlock type="sub-summary" logo='https://yt3.googleusercontent.com/n5DRh94eycw6xGcOKTn6LKQwztTwaw24fXPniFTXA3VPgwJaiOFdBwJNtXRHYUf7OdEAk9upwH0=s900-c-k-c0x00ffffff-no-rj' srcName="CNN"/>
      </div>
    </>
  )
}

export default App
