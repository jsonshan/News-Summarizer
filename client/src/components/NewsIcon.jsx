import React from 'react'
import "../styles/NewsIcon.css"
function NewsIcon({itemSrc, itemName}) {
  return (
    <div className="item-cards">
        <img src={itemSrc}/>
        <p>{itemName}</p>
    </div>
  )
}

export default NewsIcon