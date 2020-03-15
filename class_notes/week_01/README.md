# Content


# Full Stack
  > 全端 = 前端 + 後端
  
在前後端的區分中，會涉及到兩個角色：Server（伺服器、網路主機）與使用者

Server是存放寫好的程式碼，讓它們可以運作的地方，當使用者輸入網址連到 Server 時， Server 就會開始默默運作，執行程式與儲存資料，這就是所謂的「後端」。\
當處理完之後，再印出來呈現給使用者看，丟到使用者面前的就是「前端」

- 前端（Front End）：目標是要根據網頁設計師的設計圖，建立流暢、友善的使用者介面，讓使用者可以順利地與產品互動，找到並使用網站上的各種功能（**面向使用者**的功能、互動以及介面呈現）
  > 著重**畫面＆使用者的互動功能**
  
  - 使用之程式語言：
    
    ![](https://github.com/vanikk06/FinTech/blob/master/class_notes/week_01/image/Snipaste_2020-03-15_21-11-53.png)
      - HTML：標籤語言（Markup Language），用來描述網站的架構、資訊
        > 網頁畫面的架構
      - CSS：樣式表（StyleSheet），用來控制網站顯示的樣式，包含字型、顏色、背景...等等
        > 美化架構
      - JavaScript：一個用途很廣泛的程式語言，從網頁、伺服器、遊戲甚至是VR，都可以看到它的應用（最多人使用於網頁端）
        > 做與使用者的互動
          
          一開始學習網頁端時，常見的實務作法會搭配一個強大的函式庫（Library）JQuery 學習，簡單來說，JQuery 是一個讓 JavaScript 語法可以與網頁中 HTML＆CSS 連結的工具
          
          除此之外，JavaScript 在網頁操作上還有很多好用的工具  E.g.三個框架 Angular.js、Vue.js、React.js
  - 相關名詞：
     > [Learning more_UI/UX](https://gremlinworks.com.tw/ui-ux/ui-ux-comparison/)
     - static web pages：靜態網站，網頁中沒有提供使用者跟網頁互動的功能
     - dynamic web pages：動態網站，網頁提供使用者與網頁互動的相關功能
     - UI（User Interface）：**使用者介面**，設計頁面上的功能，顧及使用的便利性與整體的**設計美學，維持並創造網站的美觀性**
       > 產品的呈現
     - UX（User Experience）：**使用者經驗**，是根據使用者的習慣，**安排整個網站頁面的內容規劃**
       > 使用者體驗的過程
  
- 後端（Back End）：目標就是處理資料，讓伺服器在茫茫資料海中，最快速地做出適合的運算，提供使用者想要的資料
  > 著重**邏輯運算與資料儲存**
 
  - 使用之程式語言（較多）：
     
     ![](https://github.com/vanikk06/FinTech/blob/master/class_notes/week_01/image/Snipaste_2020-03-12_01-38-03.png)
     
   - 相關名詞：
      - Ruby on Rails（RoR）：
        - Rails：是一種「網頁開發的框架」，運用 Ruby 撰寫
      - 網頁開發框架：通常像是整理好的一堆資料夾，與一些預先為網頁開發寫好的小工具
     
- [全端](https://www.w3schools.com/whatis/whatis_fullstack.asp)

#### Source
[全端開發者神話](https://www.ithome.com.tw/voice/97360)

[What is Full Stack?](https://www.w3schools.com/whatis/whatis_fullstack.asp)

[前端、後端、全端工程師 必備技能與就業門檻比一比](https://tw.alphacamp.co/blog/2018-07-20-18464)

[網頁新手入門：初探網頁架構和前後端語言](https://medium.com/appworks-school/%E7%B6%B2%E9%A0%81%E6%96%B0%E6%89%8B%E5%85%A5%E9%96%80-%E5%88%9D%E6%8E%A2%E7%B6%B2%E9%A0%81%E6%9E%B6%E6%A7%8B%E5%92%8C%E5%89%8D%E5%BE%8C%E7%AB%AF%E8%AA%9E%E8%A8%80-a88a5dc86ee3)

[什麼是前端？什麼是後端？](https://15days.website/posts/frontend-vs-backend)

[UX/UI傻傻分不清楚？其實差很多！](https://gremlinworks.com.tw/ui-ux/ui-ux-comparison/)

[🍅](https://github.com/vanikk06/FinTech/tree/master/class_notes/week_01#content)

# DevOps
  > Development（開發） + Operations（營運維護）

DevOps 可以說是「開發」、「測試」、「維運」三者的結合，主要目的是確保網站營運的可靠性和安全性，並同時兼顧軟體開發交付的效率（「開發」與「維運」容易產生的衝突）

![](https://github.com/vanikk06/FinTech/blob/master/class_notes/week_01/image/Snipaste_2020-03-15_22-57-13.png)
> - QA（Quality Assurance）：測試，是開發到維運的必要流程，也是需要與開發和維運緊密合作的重要角色，因此經常與 DevOps 放在一起討論

- DevOps 目標：兼顧產品上限的**速度**與**品質**
- DevOps 要領：CALMS
  - Culture：文化，DevOps並非一種技能，而是跨團隊或跨技能的緊密合作文化
    > 開發多去想維運面，維運多去想開發面
  - Automation：自動化，是Dev和Ops合作的潤滑劑
  - Lean/Learn：精實/學習，精實概念可以[精實軟體開發的七大原則解釋](https://ithelp.ithome.com.tw/articles/10184557)
  - Measurement：測量，改變的依據，提示團隊如何做更正確的改善
  - Sharing：分享，DevOps是一種文化，而分享是創造 DevOps文化的最好方法，也是增加團隊透明度的好方法 

#### Source
[什麼是 DevOps？](https://azure.microsoft.com/zh-tw/overview/what-is-devops/)

[ALPHAcamp_DevOps 工程師](https://tw.alphacamp.co/blog/2018-07-20-18464#w-node-6ab77b8879a0-215075ab)

[🌶](https://github.com/vanikk06/FinTech/tree/master/class_notes/week_01#content)

# KANO Model
  > 狩野模型

日本品管大師狩野紀昭（Noriaki Kano）於1984年提出「二維品質模式」，也稱為「狩野模型」（Kano model），藉由劃分產品品質的層次，逐一分析"產品功能"與"顧客滿意度"之間的相關性，從而找到能夠有效提高顧客滿意度的功能，據以排定產品功能改善的優先順序。

打破過去品質理論的線性思維，認為只要產品品質提升，顧客滿意度也會隨之提高的想法。\
Kano model，以**滿意度**（顧客的主觀感受）和**功能**（產品的客觀機能）為兩條軸線，畫出二維平面。

![](https://github.com/vanikk06/FinTech/blob/master/class_notes/week_01/image/Snipaste_2020-03-16_02-30-38.png)

- 四個品質要素：
  - 無差異品質（indifference）：顧客不敏感、不重視的品質
    > 不提供也無所謂，可以考慮不必提供
    
    就算產品功能再強、服務再好，顧客滿意度也不會提高。\
    E.g. 買手機送3個月的手機答鈴
  
  - 一維品質（one-dimensional）：與顧客滿意度呈線性關係的品質要素
    > 成正比，與顧客滿意度直接相關
    
    品質愈好，顧客滿意度愈高；品質下滑，顧客也會給予負面評價。\
    E.g. 餐點加量不加價，顧客滿意度提高；產品容量少於標示，引起顧客不滿
  
  - 魅力品質（attractive）：顧客意想不到且創造高度滿意度的品質要素
    > 創造出的
  
    此要素還不存在時，顧客並不會意識到，但當品質一提升，顧客滿意度就會大幅提高。\
    E.g. 智慧型手機的觸控面板，原本無此需求，一推出顧客就深受此功能吸引
  
  - 必要條件品質（must-be）：產品一定要具備的功能
    > 基本需求，多做無用
    
    顧客對產品的基本需求，功能充足時，顧客覺得理所當然，但是品質不佳時，滿意度就會大幅滑落。

依據 Kano model ，可以區分出產品功能或服務的品質屬性，區分出令顧客「有感」與「無感」的品質要素，並建立改善的優先順序。
- 重要程度：必要條件品質 → 一維品質 → 魅力品質 → 無差異品質
  - 必要條件品質：首要改善對象，改善可以大幅降低顧客的不滿意程度，但只要達到基本門檻即可，持續提升顧客也沒有感覺
  - 一維品質：產品分級的標準，與顧客滿意度直接相關，應盡力提供
  - 魅力品質：Kano model最大的特色，企業應該的前進方向（品質管理 → 品質創造）
    - 品質控制：指符合客戶的基本需求
    - 品質管理：講求顧客滿意
    
      但未來僅靠品質管理難以維持企業競爭力，因此更要創造顧客意想不到的魅力品質，才能大幅提高顧客滿意度。
      
  - 無差異品質：可以考慮不用提供

隨著技術的演進與市場的發展，品質要素的分類要會改變（往圖表右下方移動）
- 魅力品質 → 一維品質 → 必要條件品質 → 無差異品質

#### Source
[狩野模型｜經理人](https://www.managertoday.com.tw/glossary/view/192)

[🍆](https://github.com/vanikk06/FinTech/tree/master/class_notes/week_01#content)

# Google Sprint


[🌽](https://github.com/vanikk06/FinTech/tree/master/class_notes/week_01#content)
