library(shiny)
library(tidyverse)
library(ggplot2)
library(shinythemes)
library(tools)
library(toOrdinal)

d <- read.table('./data/count1.txt')
d <- data.frame(d)
d$season <- 1

d2 <- read.table('./data/count2.txt')
d2 <- data.frame(d2)
d2$season <- 2

d3 <- read.table('./data/count3.txt')
d3 <- data.frame(d3)
d3$season <- 3

d4 <- read.table('./data/count4.txt')
d4 <- data.frame(d4)
d4$season <- 4

d5 <- read.table('./data/count5.txt')
d5 <- data.frame(d5)
d5$season <- 5

d6 <- read.table('./data/count6.txt')
d6 <- data.frame(d6)
d6$season <- 6

d7 <- read.table('./data/count7.txt')
d7 <- data.frame(d7)
d7$season <- 7

d8 <- read.table('./data/count8.txt')
d8 <- data.frame(d8)
d8$season <- 8

d9 <-  read.table('./data/count9.txt')
d9 <-  data.frame(d9)
d9$season <- 9

total <- rbind(d, d2, d3, d4, d5, d6, d7, d8, d9)

total <- total[order(total$V1),]

sumdf = aggregate(total$V2, by = list(total$V1), FUN = sum)
sumdf$rank[order(-sumdf$x)] <- 1:nrow(sumdf)

# Define UI for application that draws a histogram
ui <- fluidPage(
  theme = shinytheme("readable"),
   
   # Application title
   titlePanel("Character Mentions in The Office"),
#  tags$style(type='text/css', ".selectize-dropdown-content {max-height: 600px; }"), 
   
   # Sidebar with a slider input for number of bins 
     tabsetPanel(
       tabPanel("By Season",
          sidebarLayout(
          sidebarPanel(
             sliderInput("characters",
                         "Number of characters:",
                         min = 1,
                         max = 35,
                         value = 10),
             radioButtons("season",
                          "Season:",
                          choices = c("All", 1,2,3,4,5,6,7,8,9)),
             width = 2
      ),
      
      # Show a plot of the generated distribution
      mainPanel(
         plotOutput("totalmentions")
      )
   )),
   tabPanel("By Character",
            fluidPage(
              sidebarPanel(
                br(),
                selectInput("name",
                            "Character:",
                            choices = unique(total$V1)),
                br(),
                uiOutput("chartext"),
                           width = 2),
              fluidRow(
                br(),
                  splitLayout(cellWidths = c("10%", "60%", "30%"),
                              br(),
                              plotOutput("charplot"),
                              br()),
                br(),
                splitLayout(cellWidths = c("49%", "2%", "49%"),
                            plotOutput("subjectplot"),
                            br(),
                            plotOutput("personplot")),
                br(),
                br()
              ), width = 11)
            ))
)



# Define server logic required to draw a histogram
server <- function(input, output) {
  

    
    selectedseason <- reactive({if(input$season == "All"){
      total} else {
        subset(total, season %in% input$season)}})
    
    chartotals <-  reactive({aggregate(selectedseason()$V2, by = list(V1 = selectedseason()$V1), FUN = sum)})
    
    plotdf = reactive({head(arrange(chartotals(),desc(x)), n = input$characters)})
    
    output$totalmentions <- renderPlot({
      ggplot(plotdf()) +
        geom_col(aes(reorder(plotdf()$V1, -plotdf()$x), plotdf()$x),fill = "#325999") +
        labs(x = "Character",
             y = "Count",
             title = titletext()) +
        theme_minimal() + 
        theme(plot.title = element_text(size = 20, hjust = .5),
              axis.title.x = element_blank(),
              axis.title.y = element_blank(),
              axis.text.x = element_text(size = 16, angle = angle(), hjust = hjust()),
              axis.text.y = element_text(size = 16)) +
        guides(fill = FALSE)

   })
    
    titletext <-  reactive({
      if(input$season == "All"){
        paste("Total Character Mentions: All Seasons")
      } else {
        paste("Total Character Mentions: Season", input$season)
      }
    })
    
    angle <-  reactive({
      if(input$characters < 18){
        NULL
      } else {
        45
      }
    })
    
    hjust <- reactive({
      if(input$characters < 18){
        .5
      } else {
        1
      }
    })
    
    selectedchar <- reactive({subset(total, V1 %in% input$name)})
    
    
    output$charplot <- renderPlot({
      ggplot(selectedchar()) +
        geom_line(aes(x = season, y = V2)) +
        geom_point(aes(x = season, y = V2), size = 4, color = "#325999") +
        labs(x = "Season",
             y = "Count",
             title = paste(sep = "", input$name, "'s Total Mentions By Season")) +
        theme_minimal() + 
        theme(plot.title = element_text(size = 20, hjust = .5),
              axis.title.x = element_text(size = 18),
              axis.title.y = element_blank(),
              axis.text.x = element_text(size = 16),
              axis.text.y = element_text(size = 16)) +
        guides(fill = FALSE) +
        scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9)) 
    })
    
    speakerdf = read.table('./data/mentionagg.txt', header = TRUE)
    
    speakerdf = data.frame(speakerdf)
    
    speakerdf$name = toTitleCase(as.character(speakerdf$name))
    speakerdf$speaker = toTitleCase(as.character(speakerdf$speaker))
    
    selectedobject <- reactive({subset(speakerdf, name %in% input$name)})
    
    output$subjectplot <- renderPlot({
      ggplot(selectedobject()) +
        geom_col(aes(reorder(speaker, -count), count), fill = "#325999") +
        labs(x = "Character",
             y = "Count",
             title = paste(sep = "", "Who says ", input$name,  "'s name?")) +
        theme_minimal() +
        theme(plot.title = element_text(size = 20, hjust = .5),
              axis.title.x = element_blank(),
              axis.title.y = element_blank(),
              axis.text.x = element_text(size = 16),
              axis.text.y = element_text(size = 16)) +
        guides(fill = FALSE) 
    })
    
    persondf = read.table('./data/speaker.txt', header = TRUE)
    persondf = data.frame(persondf)
    persondf$speaker = toTitleCase(as.character(persondf$speaker))
    persondf$object = toTitleCase(as.character(persondf$object))
    persondf = persondf[order(persondf$speaker, -persondf$count),]
    personplotdf <- reactive({subset(persondf, speaker %in% input$name)})
    ppdf = reactive({head(arrange(personplotdf(),desc(count)), n = 10)})
    
    output$personplot <- renderPlot({
      ggplot(ppdf()) +
        geom_col(aes(reorder(object, -count), count), fill = "#325999") +
        labs(x = "Character",
             y = "Count",
             title = paste(sep = "", "Which names does ", input$name,  " say?")) +
        theme_minimal() +
        theme(plot.title = element_text(size = 20, hjust = .5),
              axis.title.x = element_blank(),
              axis.title.y = element_blank(),
              axis.text.x = element_text(size = 16),
              axis.text.y = element_text(size = 16)) +
        guides(fill = FALSE) 
    })
    
    chardf <- reactive({subset(sumdf, Group.1 %in% input$name)})
    
    output$chartext <- renderUI({ str1 <- paste(strong("Total mentions: "),
                                                      chardf()$x,
                                                      br(),
                                                      strong("Rank: "),
                                                      toOrdinal(chardf()$rank),
                                                      "out of",
                                                      nrow(sumdf))
                                                
                                  HTML(paste(str1[1]))
                                                    })
    
}



# Run the application 
shinyApp(ui <- ui, server <- server)

