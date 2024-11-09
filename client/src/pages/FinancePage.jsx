import React from 'react'

function FinancePage({sources}) {
  return (
    <div className='FinancePage'>
      <h3 className="sub-title">News Sources</h3>
      <NewsSource sources={sources}/>
      <h3 className="sub-title">Summary</h3>
      <TextBlock type="main-summary"/>
      <h3 className="sub-title">Summary (Separate Sources)</h3>
      <TextBlock type="sub-summary" logo='https://yt3.googleusercontent.com/n5DRh94eycw6xGcOKTn6LKQwztTwaw24fXPniFTXA3VPgwJaiOFdBwJNtXRHYUf7OdEAk9upwH0=s900-c-k-c0x00ffffff-no-rj' srcName="CNN"/>
    </div>
  
  )
}

export default FinancePage