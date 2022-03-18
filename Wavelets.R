list.packages <- c("WaveletComp", "ggplot", "tidyverse")

if (!require("pacman")) {
    install.packages("pacman")
    library("pacman")
    }
pacman::p_load("WaveletComp", "ggplot2", "tidyverse")
dir_dados <- paste0(getwd(), "/Dados/SPI12-Dez.csv")

spi_12 <- read.csv(dir_dados, sep = ";", header = FALSE)

b1_df <- seq(1950, 2016)
b2_df <- seq(1950, 2016)
b3_df <- seq(1950, 2016)
coords <- spi_12[(1:2), ]

for (i in (2:ncol(spi_12))) {

    data_wavelets <- data.frame(SPI12 = spi_12[(-2:-1), i])

    wavelets <- analyze.wavelet(
        data_wavelets, my.series = "SPI12",
        loess.span = 0.5, method = "white.noise",
        dt = 1, dj = 1 / 20,
        lowerPeriod = 2,
        upperPeriod = 64,
        make.pval = TRUE, n.sim = 100
        )

    band_1 <- reconstruct(
        wavelets, sel.lower = 2, sel.upper = 8,
        show.legend = FALSE, only.coi = F,
        rescale = FALSE, only.sig = F, plot.rec = F
        )

    band_2 <- reconstruct(
        wavelets, sel.lower = 9, sel.upper = 40,
        show.legend = FALSE, only.coi = F,
        rescale = FALSE, only.sig = F, plot.rec = F
        )

    b1_rec <- data.frame(
        SPI12 = band_1$series$SPI12.r
        )
    b1_df <- cbind(b1_df, b1_rec$SPI12)

    b2_rec <- data.frame(
        SPI12 = band_2$series$SPI12.r
        )
    b2_df <- cbind(b2_df, b2_rec$SPI12)

    b3_rec <- data.frame(
        SPI12 = data_wavelets$SPI12 - b1_rec$ SPI12 - b2_rec$SPI12
        )
    b3_df <- cbind(b3_df, b3_rec$SPI12)
}
b1_df <- as.data.frame(b1_df)
b2_df <- as.data.frame(b2_df)
b3_df <- as.data.frame(b3_df)

names(b1_df)[1] <- names(coords)[1]
names(b2_df)[1] <- names(coords)[1]
names(b3_df)[1] <- names(coords)[1]

b1_df <- rbind(coords, b1_df)
b2_df <- rbind(coords, b2_df)
b3_df <- rbind(coords, b3_df)

write.table (
    b1_df, file = paste0(getwd(),"/Dados/band1.csv"),
    sep = ";", row.names = F, col.names = F
    )

write.table (
    b2_df, file = paste0(getwd(),"/Dados/band2.csv"),
    sep = ";", row.names = F, col.names = F
    )

write.table (
    b3_df, file = paste0(getwd(),"/Dados/band3.csv"),
    sep = ";", row.names = F, col.names = F
    )
