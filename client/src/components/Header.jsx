
import React, {useEffect} from 'react'
import "../styles/GenreSelection.css"
import image from "../assets/images/newsAI.png"

function Header() {
  return (
    <div className="header-container">
        <img src={image} alt="news.ai Logo" height={.1*window.innerHeight}/>
    </div>
  )
}

export default Header