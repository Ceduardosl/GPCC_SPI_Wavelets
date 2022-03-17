list.packages <- c("WaveletComp", "ggplot", "tidyverse")

if (!require("pacman")) {
    install.packages("pacman")
    library("pacman")
    }
pacman::p_load("WaveletComp", "ggplot2", "tidyverse")
dir_dados <- paste0(getwd(), "/Dados/SPI12-Dez.csv")

spi_12 <- read.csv(dir_dados, sep = ";", header = FALSE, row.names = 1)

b1_df <- seq(1950, 2016)
b2_df <- seq(1950, 2016)
b3_df <- seq(1950, 2016)
coords <- spi_12[(1:2), ]

for (i in (1:ncol(spi_12))) {

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








df <- data.frame(
    data = seq(1950, 2016),
    SPI12 = data_wavelets$SPI12
    )

ggplot() +
  theme_bw() +
  geom_line(data = df, aes(x = data, y = SPI12), color = "black") +
  geom_line(data = b1_rec, aes(x = data, y = SPI12), color = "green") +
  geom_line(data = b2_rec, aes(x = data, y = SPI12), color = "blue") +
  geom_line(data = b3_rec, aes(x = data, y = SPI12), color = "red")