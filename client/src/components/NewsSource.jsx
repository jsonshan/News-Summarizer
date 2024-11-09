import { useState } from 'react'
import "../styles/NewsSource.css"

import NewsIcon from "./NewsIcon";

function NewsSource({sources}){
    // Sources = [ [imgSrc, itemName], [imgSrc, itemName] ... ]
    return(
        <div id="news-sources-container">
            <div id="items-wrapper">
                {sources.map((e, i) => {
                    return <NewsIcon key={i} itemSrc={e[0]} itemName={e[1]}/>
                })}
            </div>
            {/* <i id="add-source-btn">+</i> */}
        </div>
    );
}


export default NewsSource;