import "../styles/NewsSource.css"


function NewsSource(){


   return(
       <div id="news-sources-container">
           <div id="items-wrapper">
               <div className="item-cards">
               <img src="https://yt3.googleusercontent.com/n5DRh94eycw6xGcOKTn6LKQwztTwaw24fXPniFTXA3VPgwJaiOFdBwJNtXRHYUf7OdEAk9upwH0=s900-c-k-c0x00ffffff-no-rj"/>
               <p>Source name</p>
               </div>
               <div className="item-cards">
                   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/1280px-Fox_News_Channel_logo.svg.png"/>
                   <p>Source Name</p>
               </div>
           </div>
           <i id="add-source-btn">+</i>
       </div>
   );
}


export default NewsSource;