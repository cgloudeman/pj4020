library(ggplot2)
library(tidyverse)

contenders <- read.csv(file = "pj_contenders.csv", row.names = 1)
nba_champs <- read.csv(file = "NBA_champs_cities.csv", row.names = 1)

contenders['Count'] <- 0
contenders['Color'] <- 0
for (year in row.names(contenders)) {
  contenders[year,]$Count <- sum(contenders[year,] != "")-2
  contenders[year,]$Color <- ifelse(nba_champs[year,]$Champion %in% as.matrix(contenders[year,]),
                                  "Champion Won 40 Before Losing 20", "Champion Did Not Win 40 Before Losing 20")
}
contenders['2020','Color'] <- "Champion Won 40 Before Losing 20"

contenders %>% ggplot() +
  geom_col(aes(x = as.integer(row.names(contenders)), y = Count, fill = Color), 
           colour = 'black', width = 1) +
  xlab('Season') +
  ylab('Number of Teams') +
  ggtitle('NBA Teams that Won 40 Games Before Losing 20 Games') +
  scale_fill_manual(breaks = c("Champion Won 40 Before Losing 20", "Champion Did Not Win 40 Before Losing 20"), 
                    values=c("steelblue2", "orangered")) +
  theme(plot.title = element_text(hjust = 0.5), 
        legend.position = c(0.855,0.95), legend.title = element_blank())


contenders %>% ggplot() +
  geom_bar(aes(x = Count), fill = "darkorange2", colour = "black", width = 1) +
  scale_x_continuous(name = "Teams per Season", breaks = c(0,2,4,6,8)) +
  ylab("Count") +
  ggtitle("NBA Teams that Won 40 Games Before Losing 20 Games") +
  theme(plot.title = element_text(hjust = 0.5))

