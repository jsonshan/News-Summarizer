import React from 'react'
import "../styles/TextBlock.css"
function TextBlock({type, logo, srcName, text}) {
  return (
    <>
      <div className={`${type} text-block`}>
      {
        (type == 'sub-summary'
        ? 
        <>
          <div className="item-display">
            <img src={logo}/>
            <p>{srcName}</p>
          </div>
          <div className="divider"></div>
        </>
        :
          <></>
        )
      }
        <div className="text-section">
          <p>{text}</p>
        </div>
      </div>
    </>
  )
}

export default TextBlock