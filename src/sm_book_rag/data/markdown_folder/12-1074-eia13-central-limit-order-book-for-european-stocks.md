
Government

Office for

Science

# A central limit order book for European stocks

# Economic Impact Assessment EIA13

Foresight, Government Office for Science

Foresight




A central limit order book for European stocks

# Contents

1. Objective ........................................................................................................................................... 3
2. Background....................................................................................................................................... 4
1. Theory ........................................................................................................................................ 6
2. Evidence ...................................................................................................................................10
3. Risk assessment.............................................................................................................................15
4. Options............................................................................................................................................17
5. Costs, risks and benefits.................................................................................................................20
6. Future..............................................................................................................................................21
7. Summary......................................................................................................................................... 22

References ............................................................................................................................................23





# A central limit order book for European stocks

# Thierry Foucault

# HEC, Paris¹

# 5 April 2012

This review has been commissioned as part of the UK Government’s Foresight Project, The Future of Computer Trading in Financial Markets. The views expressed do not represent the policy of any Government or organisation.

¹ Thierry Foucault, HEC, Paris, Finance Department, 1 rue de la Libération, 78351 Jouy en Josas, France. Tel: (33) 1 39 67 95 65. Fax: (33) 1 39 67 70 85. E.mail: foucault@hec.fr. I am grateful to two anonymous referees for very useful comments on an earlier draft.




A central limit order book for European stocks

# 1. Objective

The Markets in Financial Instrument Directive (MiFID) in November 2007 has fostered entry of new trading platforms in European equity markets. As a result the market shares of the incumbent markets (NYSE-Euronext, The London Stock Exchange-Borsa Italiana, and the Deutsche Börse) has considerably declined and trading in the European equity market is now much more fragmented than it was before MiFID. For instance, Table 1 displays the market share of the London Stock Exchange (LSE) and its main competitors in FTSE100 stocks (which are listed on the LSE). The table shows that the LSE market share in these stocks is now close to 50% against about 80% in 2007. The same trend is observed for other incumbent markets (in particular NYSE-Euronext or the Deutsche Börse).

| Market      | Market Share |
| ----------- | ------------ |
| LSE         | 53.9%        |
| Chi-X       | 31%          |
| Turquoise   | 8%           |
| BATS Europe | 6.8%         |

Table 1. Market Shares of various markets in FTSE 100 stocks as of February 2012

Source: Fidessa

The effects of this evolution on the quality of European equity markets are debated. For instance, a survey of the CFA institute shows that its members have ambivalent views about the effects of MiFID on market illiquidity (often measured by trading costs incurred by investors in the execution of their trades; see below): the respondents are evenly spread among those who feel that MiFID decreased, increased, or had no impact on European equity markets’ illiquidity.² Moreover, 42% (resp. 26%) of the respondents believe that market fragmentation has impaired (resp. improved) price discovery for European stocks.

² See “The impact of market fragmentation under the markets in financial instruments directive”, CFA Institute, Centre for financial market integrity, 2009.

3


A central limit order book for European stocks

This is a source of concern because market liquidity and price discovery are vital for well-functioning financial markets. In more liquid markets, investors require a smaller return to invest in firms and can hold diversified portfolios at a lower cost. As a result, the allocation of risk is improved, firms can invest in more projects, and growth is enhanced. Better price discovery also guarantees a more efficient allocation of capital among investment projects.

One way to address the concerns raised by market fragmentation consists in mandating consolidation of all trades in a security in a single, fully transparent limit order book where all limit orders execute according to price and time priority (a measure known as the central limit order book or CLOB). This review assesses the costs and benefits of such a measure.

# 2. Background

In this section, I summarize the main findings of academic studies that study the benefits and costs of mandating consolidation of order flow in a central limit order book. To understand the issues addressed in these studies, it is useful to first (a) define the concept of “limit order book” and (b) describe how trades take place when a security trades simultaneously on multiple platforms. To this end, consider Example 1.

# Example 1

# (a) NYSE Euronext Limit Order Book (NSC)

| Quantity (shares) | Ask (euros) | Bid (euros) |
| ----------------- | ----------- | ----------- |
| 700               | 43          |             |
| 400               | 42.97       |             |
| 500               | 42.96       |             |
| 1000              | 42.94       |             |
| 600               | 42          |             |




# A central limit order book for European stocks

# (b) BATS Europe Limit Order Book

| Quantity (shares) | Ask (euros) | Bid (euros) |
| ----------------- | ----------- | ----------- |
| 100               | 43          |             |
| 600               | 42.98       |             |
| 300               | 42.95       |             |
| 100               | 42.93       |             |
| 500               | 42          |             |

This example considers a stock XYZ that trades on two trading platforms, NSC (NYSE-Euronext’s trading platform) and BATS Europe (another platform where stocks listed on Euronext can be traded). The two tables display bid and ask prices for stock XYZ and the number of shares demanded or supplied at these prices in each trading platform at a given point in time. These sets of offers are called the limit order books for stock XYZ on NYSE-Euronext and BATS Europe, respectively.

Offers to sell or to buy stock XYZ in these limit order books are called limit orders. For instance, the sell limit order at €42.95 in BATS Europe indicates that one investor (or several investors) is willing to sell up to 300 shares at that price. Similarly, the buy limit order at €42.94 for 1000 shares in NYSE-Euronext indicates that one or several investors are willing to buy up to 1000 shares at that price. Limit order books are continuously updated as investors (or their brokers) submit new limit orders, cancel previously placed limit orders, or trades occur when an investor submits a market order. For instance, suppose that one investor wishes to immediately buy 900 shares of stock XYZ. The investor can execute this trade by submitting a buy market order for 900 shares, which is an instruction to immediately buy this number of shares at the best possible price.

When a stock is traded in multiple markets, the broker in charge of the execution of an order must decide to which market he will direct (“route”) his client’s order. A broker has at least three ways to execute a buy market order for 900 shares given the limit order books shown in Example 1. First, he could route the market order to NSC only. In this case, the order will


A central limit order book for European stocks

execute for 500 shares at €42.96 and then for 400 shares at the next best offer on NSC, i.e., €42.97. Indeed, in a limit order book, strict price priority is enforced: best priced limit orders are executed before less aggressively priced orders until full execution of the market order. In this case, the average “execution” (i.e., purchase) price for the investor is then €42.964. Alternatively, the broker can route the order to BATS Europe only, in which case the investor’s market order executes at an average execution price of €42.97. Finally the broker can place a buy market order for 300 shares in BATS Europe and another buy market order for 600 shares in NSC. With this “routing” strategy, the average execution price for the investor is €42.95. In fact, among all possible routing strategies, this strategy yields the best (i.e., smallest) execution price for the investor.

In order to gauge the performance of a trading mechanism, one needs a metric. One possibility is to study whether investors’ welfare is higher or not when trading is centralized in a single limit order book. Measuring investors’ welfare empirically is difficult, however. Hence, economists and practitioners use measures of market performance that are more easily observed. In particular, they often rely on measures of market illiquidity: the quoted bid-ask spread, the effective bid-ask spread, or market depth.

1. The quoted bid-ask spread is the difference between the best ask price and the best bid price. For instance the bid-ask spread in NSC is 42.96-42.94=0.02. When a stock trades in multiple markets, the quoted bid-ask spread across markets (the “consolidated” spread) is potentially a better measure of illiquidity.
2. The effective bid-ask spread is twice the difference between the average execution price for a market order and the midquote when the order gets executed, multiplied by +1 for a buy market order and -1 for a sell market order.3 Bid-ask spreads (quoted or effective) measure implicit trading costs for investors submitting market orders (an investor buying a security and reselling it immediately bears a cost equal to the bid-ask spread). Large implicit costs are associated with a less liquid market.
3. Market depth is the number of shares offered at the best quotes or up to a certain number of ticks behind the best quotes. Intuitively, when market depth is large, investors can execute market orders of large size without moving prices much. Hence, greater depth is associated with a more liquid market.

# 2.1. Theory

A critical issue is whether consolidation of order flow in a single limit order book results in higher or lower liquidity for a stock, compared to a situation in which the stock trades in multiple limit order books. Glosten (1994) is the first theoretical paper to shed light on this question. His theory yields a surprising result: the limit orders posted in the market are exactly the same whether all offers are consolidated in a single limit order book or scattered among multiple limit order books. Hence, in terms of liquidity, Glosten (1994)’s theory implies that the number of co-existing limit order books for a stock is irrelevant: implicit trading costs for investors submitting market orders do not depend on this number. This irrelevance result depends on various assumptions. In particular Glosten (1994) assumes that:

1. The number of investors submitting limit orders is very large so that competition drives their expected profits to zero.

For instance, consider the buy market order for 900 shares in Example 1. If this order executes only in Euronext, the effective bid-ask spread for this trade is 2×(42.964-42.945)=0.038.




A central limit order book for European stocks

2. Investors can split their orders between markets without costs. This implies for instance that there is no membership cost and investors have free and full information on the limit orders posted in each market.

3. Trading and clearing fees do not depend on the number of competing platforms (in fact in Glosten (1994), there is no trading fee).

Subsequent research has analyzed what happens when these assumptions are relaxed. Biais, Martimort, Rochet (2000) relax the first assumption. Specifically, they assume that the number of investors submitting limit orders (liquidity providers) is limited. As a result, competition among limit order submitters is imperfect and each liquidity provider can exert pricing power in choosing his schedule of limit orders. In this case, liquidity providers earn rents in equilibrium, at the expense of investors submitting market orders (liquidity demanders).4 When the number of liquidity providers becomes large, these rents vanish and the equilibrium is identical to that obtained in Glosten (1994).

Biais, Martimort and Rochet (2000) also show that Glosten (1994)’s irrelevance result still holds when competition among limit order traders is imperfect. The reason is that investors have costless access to all limit order books. Hence, from investors’ point of view, everything is as if all limit orders were consolidated in a single market. As a result, investors (those submitting market orders and those submitting limit orders) behave in the same way whether limit orders are centralized in one market or not.

Biais, Martimort and Rochet (2000) assume that the number of liquidity providers is independent of the number of platforms (i.e., remains the same whether there is one or, say, ten trading platforms competing together). In reality, however, an increase in the number of trading platforms might expand the pool of liquidity providers. Suppose for instance that a single platform operates a CLOB. By restricting entry of liquidity providers, the platform softens competition among liquidity providers and increases their rent. This strategy can increase the trading platform’s revenue as the latter recovers a fraction of liquidity providers’ rent by charging fees for its trading services. Thus, one drawback of a CLOB is that it might, indirectly, lead to a less competitive outcome.

Biais, Martimort and Rochet (2000) also assume that the set of possible prices for limit orders is continuous. This assumption is not innocuous as shown by Foucault and Menkveld (2008). They consider a model in which, as in reality, investors submitting limit orders must position their quotes on a pre-determined grid (market participants refer to the minimum difference between two quotes on the grid as being the “tick size”).

Foucault and Menkveld (2008) first analyze the case in which all trades must take place in a CLOB (call this market “the incumbent” market). At each price, investors fill the limit order book until the point at which the expected profit on the marginal limit order (i.e., the order with the lowest priority of execution at each price) is just zero.5 Infra-marginal limit orders at a given

4 Biais, Bisière and Spatt (2010) provide empirical evidence supporting the view that competition among liquidity providers is imperfect in limit order markets.

5 In Foucault and Menkveld (2008), the expected revenue on the marginal limit order posted at a given price declines with the total number of shares offered at this price because the likelihood of execution of the marginal limit order declines as the total number of shares offered at a price increases. At some point, this expected revenue just covers the fixed order submission cost borne by an investor when he submits a limit order and the expected profit of the marginal limit order is then just zero.




# A central limit order book for European stocks

Price (orders with a higher priority of execution) obtain a strictly positive expected profit as long as the tick size is strictly positive.

In a second step Foucault and Menkveld (2008) consider the case in which a second limit order market is opened (call this new market the “entrant” market). They show that entry of this second market reduces implicit trading costs (by raising the number of shares supplied or demanded at each posted price in the market) as long as the tick size is strictly positive. The reason is that the absence of time priority across markets intensifies competition among investors submitting limit orders. For instance, consider an investor with a sell limit order at the end of the queue of limit orders at the best ask price (say €100) in the incumbent market and suppose that there is yet no sell limit order at this price in the entrant market. The likelihood of execution of the investor’s order is small relative to the limit order at the top of the queue (the order with the highest priority of execution). As a result, the expected profit of this investor is small. In this case, the investor can bypass the priority of execution of the limit order at the top of the queue by submitting a limit order at €100 in the entrant market. This “queue-jumping strategy” raises his execution probability and therefore his expected profit, other things equal. Queue-jumping intensifies competition among investors submitting limit orders and ultimately reduces their rents. As these rents are obtained at the expense of investors submitting market orders, implicit trading costs decline relative to the case in which all trades take place in a CLOB.

Foucault and Menkveld (2008) also relax the assumption that all investors can split their market orders between competing limit order books at no cost. Specifically, they assume that only a fraction of investors (that they call “smart routers”) have access to both markets while remaining investors only trade in the incumbent market. This assumption captures the fact that some investors or brokers may find it too costly (at least in the early stages of the entrant market) to split their market orders between both markets. Foucault and Menkveld (2008) show that the liquidity of the entrant market and the consolidated market increases in the fraction of smart routers. Indeed, the likelihood of execution for limit orders in the entrant market increases in the fraction of smart routers. As a result, the higher this fraction, the higher are investors’ incentives to post aggressive limit orders in the entrant market and the more intense is competition between liquidity providers in both markets. This result underscores the importance of facilitating access of all investors to all platforms in competition.

Competition among limit order markets is often viewed as a way to force exchanges to charge more competitive trading fees. Consistent with this view, the entry of new trading platforms in the U.S. and in Europe has been followed by a dramatic reduction in trading fees. Colliard and Foucault (2011) analyze how inter-market competition affects trading fees, liquidity, and investors’ welfare. They consider two different market structures for a security. In the first market structure, the stock trades in a CLOB. In the second market structure, the stock trades in two different limit order markets. In both market structures, investors can optimally choose to submit market or limit orders and trading platforms optimally choose their trading fees, accounting for their effect on investors’ order submission choices.

For instance, in a recent consultation paper, the SEC notes that: “Mandating the consolidation of order flow in a single venue would create a monopoly and thereby lose the important benefits of competition among markets. The benefits of such competition include incentives for trading centers to create new products, provide high quality trading services that meet the need of investors and keep trading fees low.” (see page 11, in "Concept Release on Equity Market Structure", SEC (2010)).


# A central limit order book for European stocks

Colliard and Foucault (2011) show that competition among trading platforms drives their trading fee to the competitive level (zero in their model). In contrast, a single platform (a CLOB) takes advantage of its monopolistic position to charge a high fee, extracting rents from investors. In their model, bid-ask spreads adjusted for trading fees increase in the size of trading fee. As a result, bid-ask spreads adjusted for fees are higher with a CLOB than when investors have access to multiple competing limit order markets. Thus, the market is less liquid in a CLOB.

# Summary

Overall, these theoretical analyses do not provide much support for mandating a CLOB. At best, this measure will have no effect on market liquidity (Glosten (1994) and Biais, Martimort, Rochet (2000)). At worst, it impairs market liquidity because it has a negative effect on the intensity of competition among liquidity providers (Foucault and Menkveld (2008)) or because the operator of a CLOB can take advantage of its monopolistic position to charge too high fees (Colliard and Foucault (2011)). All these models stress the importance of easy (i.e., at low cost) access for investors to the various platforms on which a stock is traded. This is a requisite to reap the full benefits of inter-market competition.

These conclusions are at odds with the claim that market fragmentation is harmful for market liquidity.

Advocates of this view often argue that securities markets are characterized by so called “thick market externalities” (or network effects). That is, an investor expects a higher benefit from trading in a market when the number of participants in this market increases. Thick market externalities may arise from risk sharing concerns as in Pagano (1989) (investors can better hedge their risk exposure in large markets) or asymmetric information as in Admati and Pfleiderer (1988) (a market with a large number of uninformed investors is more liquid). In addition, the higher the number of participants to a market, the smaller the per capita fixed cost of running the market. If this reduction in cost is passed to investors (through lower trading fees or bid-ask spreads) then investors are better when the number of market participants increases (see Pagano and Padilla (2006)).

In the presence of thick market externalities, investors’ welfare and market liquidity are often maximized by concentrating all trades in one market. Hence, in the presence of thick market externalities, a CLOB may dominate the situation with multiple competing limit order book markets. This conclusion however hinges on one key assumption: investors cannot simultaneously participate in all markets (that is, the cost of participating to multiple markets is high, at least for some investors). If instead they can, as assumed in the models described in the first part of this section (Glosten (1994), Biais, Martimort and Rochet (2000) etc…) then investors are effectively in contact with all other investors and concentration of trading in a single market is not necessary to take full advantage of thick market externalities. What matters is not concentration of trading in a single market per se but rather easy access to all trading platforms by all investors.

There are additional reasons for which market fragmentation may impair market liquidity. First, it increases investors’ “search costs,” that is, the cost of identifying the strategy that will enable them to execute their order at the best possible price. For instance, in the current market structure for European equities markets, investors must either use costly datafeed and smart order routing technologies or delegate the execution of their trades to brokers to best harness the liquidity available in the different trading platforms for a stock. This raises several problems: (i) the cost of searching for best execution in a fragmented market may exceed the benefit in terms of improved consolidated liquidity; (ii) some investors may decide not to pay this cost and trade only on the incumbent exchange; this is problematic since market fragmentation may


A central limit order book for European stocks

enhance consolidated liquidity and yet decreases the liquidity available in the incumbent market (Foucault and Menkveld (2008)); (iii) agency problems between brokers and their clients become more acute when it is more costly for investors to check whether they obtained the best possible execution on a given trade.

Madhavan (1995) points another problem associated with market fragmentation. If information on transactions in one trading venue for a security is not quickly and easily available to market participants in other trading venues then market fragmentation gives local market power to liquidity suppliers in each platform and increases informed investors’ ability to exploit their information. These two effects tend to make fragmented markets less liquid.

In order to mitigate these drawbacks of market fragmentation, one must therefore develop very efficient inter-market linkages so as (i) to minimize investors’ search cost and (ii) increase the speed at which information on transaction prices flow between these venues.

Theories surveyed so far are silent on the effects of market fragmentation on informational efficiency and price discovery. I am not aware of a theoretical comparison of price discovery when trades concentrate in a CLOB and when they can happen in multiple competing limit order books. A few academic studies analyze the effect of market fragmentation on price discovery, however.7 Chowdhry and Nanda (1991) consider a model in which fragmentation reduces market liquidity (because some investors, called non-discretionary traders by Chowdhri and Nanda (1991), cannot simultaneously participate to all markets) but improves informational efficiency (see also Foucault and Gehrig (2008)). In contrast, Madhavan (1995) shows that market fragmentation can impair price discovery. Thus, it is not clear theoretically whether market fragmentation is harmful or beneficial for price discovery.

# 2.2. Evidence

I now discuss academic studies that provide evidence on whether mandating consolidation of trades in a CLOB could improve market liquidity. These studies fall in four broad categories:

1. Studies that compare measures of market liquidity for a security before and after a shift from a CLOB to a multi-market environment. To my knowledge Foucault and Menkveld (2008) is the only study of this type.
2. Studies that compare measures of market liquidity before and after entry of a new trading venue in the market for a security. Several studies consider an event of this type (e.g., deFontnouvelle et al. (2003), Boehmer and Boehmer (2003) and Gresse (2011)).
3. Studies that relate measures of market liquidity for a security to measures of market fragmentation for this security (e.g., O’Hara and Ye (2010), Gresse (2011) and Degryse et al. (2011)).
4. Studies that compare market liquidity before and after the merger of exchanges (Arnold et al. (1999), Pagano and Padilla (2006) and Nielsson (2009)).

Foucault and Menkveld (2008) study the entry of the London Stock Exchange into the Dutch equity market with the launch of EuroSETS, an electronic limit order market. Before entry of EuroSETS (on April, 23 2004), trading was largely centralized in NSC, the limit order market operated by Euronext. Thus, the introduction of EuroSETS offers the opportunity to study

7 These studies do not specifically apply to limit order markets.




A central limit order book for European stocks

empirically whether switching from a centralized limit order book to a more fragmented environment impairs or improves liquidity.

Foucault and Menkveld (2008) focus their analysis on 25 stocks constituents of the AEX index. Their methodology consists in comparing measures of quoted spreads, effective spreads, and depth for these stocks before and after the entry of EuroSETS, while controlling for changes in other variables affecting liquidity (volatility, stock price level, etc…). They find that quoted spreads are not much affected by the entry of EuroSETS (changes in quoted spreads are either not significant and when they are, these changes point to a reduction in quoted spreads). In contrast, the cumulative depth (number of shares) posted at each price point in the market (consolidated across the two markets) increases very substantially. For instance, for the quartile of most actively traded stocks in their sample, Foucault and Menkveld (2008) find an increase of about 46% to 100% (depending on the period of observation) in the number of shares posted at the best quotes in the market. These results suggest that the introduction of EuroSETS has substantially improved the liquidity of the consolidated market. Interestingly, there is no decline in liquidity in Euronext limit order book. Foucault and Menkveld (2008) attribute these findings to two effects: (i) an escalation of competition among limit order traders and (ii) the reduction in trading fees that followed the entry of EuroSETS.

I now turn to studies that consider the entry of one or several new trading venues in the market for a security. These studies typically consider securities that trade in hybrid market structures combining features of dealership markets and limit order markets. Thus, the conclusions of these studies may not necessarily apply to a shift from a CLOB to a market structure characterized by multiple competing limit order books. Yet, they shed light on how inter-market competition affects market liquidity.

Until 1999, there was not much inter-market competition among U.S. options exchanges. Indeed, stock options were often exclusively traded on the exchange where they were listed. For instance, Dell computers options were listed on the Philadelphia Stock Exchange (PSX) and traded exclusively on this exchange. This situation changed in August 1999 when the Chicago Board Options Exchange (CBOE) and the American Stock Exchange (AMEX) announced that they would start trading these options as well. This decision triggered a very intense battle for market share among U.S. options markets. Battalio, Hatsch and Jennings (2004) report that, for the 50 most actively traded options, the market share of the exchange with a monopoly position in one option class before August 1999 had fallen by about 42% one year later.

This event is interesting since, for a relatively large number of options, it corresponds to a sudden shift from a centralized trading environment to a fragmented environment, characterized by competition among multiple exchanges. De Fontnouvelle et al (2003) empirically analyze the impact of this change in market structure on quoted and effective bid-ask spreads in option markets. Their sample includes 28 options. They find that the advent of competition for order flow among options exchanges is associated with a strong decline in effective and quoted bid-ask spreads. For instance, the average declines in effective and quoted spreads for put options are equal to 38.7% and 50%, respectively.

In 1999, trading on five of the six U.S. options exchanges was taking place in open outcry markets. In open outcry markets, brokers and market-makers physically meet on a trading floor. Brokers announce the number of units they want to buy or sell and other traders respond with a price at which they are willing to accommodate the trade. The trade is ultimately split amongst those posting the best quote.




# A central limit order book for European stocks

only those present on the floor of the exchange listing this option. Hence competition among options exchanges mechanically increased the number of market-makers per option, which could be the reason for which it triggered a decline in bid-ask spreads. In line with this interpretation, DeFontnouvelle et al. (2003) note that:

“The magnitude of the spread reductions across all options classes provide evidence that intra-exchange competition is not a good substitute for inter-exchange competition, evidence that fragmented order flow across competing markets may offer important benefits to investors”

(DeFontnouvelle et al.(2003), p.2440)

Boehmer and Boehmer (2003) examine the entry of the NYSE (in April 2001) into the trading of three actively traded Exchange Traded Funds (ETFs), namely the Nasdaq-100 Trust Series I (the “QQQ”), the Standard and Poor’s Depository Receipt Trys Series I (the “SPY”), and the Dow Jones Industrial Average Trust Series I (the “DIA”), and 27 other “small” ETFs. This is an interesting event since inter-market competition in this market was already strong before the entry of the NYSE. Indeed, these ETFs were listed on the AMEX but the AMEX “specialist” (market-maker) for each ETF was already competing with specialists in these ETFs on other regional exchanges, Nasdaq market-makers, and limit orders posted for these ETFs on Electronic Communication Networks (trading platforms that operate electronic limit order books). Thus, arguably, entry of the NYSE in this market was a more marginal event than the advent of competition for order flow in the option market in 1999. Hence, one may have expected this entry to increase the costs of market fragmentation without much benefit in terms of added liquidity.

However, Boehmer and Boehmer (2003) find a large decline in effective and quoted bid-ask spreads after the entry of the NYSE. For instance, the average effective spread of the SPY ETF (averaged across all market centers where this ETF is traded) declines by about 48% after the entry of the NYSE. Moreover, the quoted depth (the number of shares supplied or demanded at the best quotes) increases significantly. These results are robust when the authors control for changes in trading volume, price levels, or volatility that occur contemporaneously with the entry of the NYSE. Boehmer and Boehmer (2003) argue that the decline in effective spreads is mainly due to a decrease in market-makers’ rents, most likely because of more intense competition in liquidity provision. Hence, as in deFontnouvelle et al. (2003), Boehmer and Boehmer (2003)’s findings suggest that inter-market competition can strengthen intra-market competition between liquidity providers.⁸

Gresse (2011) compares measure of market liquidity for 140 European stocks (constituents of the FTSE100, CAC40 and SBF120 indexes) before and after the implementation of MiFID in November 2007. Specifically, she compares average quoted spreads, effective spreads, and market depth for these stocks in October 2007 on the one hand and January, June and September 2009 on the other hand. In October 2007, the market for these stocks is not much fragmented (they are primarily traded on the exchange where they are listed) while in 2009, these stocks trade in several trading venues (the exchange on which they are listed, but also

8 Battalio (1997) also provides empirical evidence consistent with this view. He finds that the entry of a new market-maker (“Bernard L. Madoff Investment Securities”) in stocks listed on the NYSE triggered a significant reduction in the average quoted spread (consolidated across markets) for these stocks.


# A central limit order book for European stocks

Chi-X, BATS Europe, Turquoise and Nasdaq OMX). Gresse (2011) finds that quoted and effective bid-ask spreads are smaller on average after the implementation of MiFID, especially when one compares October 2007 with September 2009. This finding obtains despite the fact that volatility in 2009 is higher than in October 2007. This suggests that the escalation of intermarket competition in the post MiFID period explains at least part of the reduction in measures of bid-ask spreads.

A few other studies (O’Hara and Ye (2011), Degryse, deJong, and Van Kervel (2011) and Gresse (2011)) take another approach. They analyze how changes in an index of market fragmentation affect measures of market liquidity and sometimes price discovery.

O’Hara and Ye (2011) uses the fraction of off-exchange trading volume in a stock as an index of market fragmentation for this stock. Off-exchange volume includes trades taking place on Electronic Communication Networks operating electronic limit order books (e.g., BATS or DirectEDge) or dark pools (e.g., Millenium, Instinet, ITG Posit etc…). They use data from January to June 2008 to measure the average effective bid-ask spread and the average value of their index of market fragmentation for 262 stocks listed on Nasdaq and the NYSE. They find a strong negative cross-sectional relationship between the level of market fragmentation for a stock and the effective bid-ask spread of this stock, even after controlling for other variables that may simultaneously determine the index of market fragmentation and the effective bid-ask spread. They also compare the average effective spreads of two groups of stocks that are similar in terms of market capitalization and prices but that differ in market fragmentation. The more fragmented groups has smaller effective bid-ask spreads than the less fragmented group. The effect appears stronger for smaller stocks than larger stocks.

O’Hara and Ye (2011) also show that the short run price volatility price is higher for stocks with a higher index of market fragmentation. However, this increase in volatility does not seem to harm price discovery. In fact, for stocks listed on Nasdaq, O’Hara and Ye (2011) find a positive association between their index of market fragmentation and a measure of the efficiency of price discovery.

Degryse et al. (2011) consider a sample of 52 Dutch stocks (large and mid-cap) over the 2006-2009 period. This period is interesting since, after 2007, the European market became significantly more fragmented due to the implementation of MiFID. The stocks in their sample are listed on Euronext Amsterdam and trade on Chi-X, Deutsche Börse, Turquoise, BATS trading, Nasdaq OMX and SIX Swiss Exchange. They measure market fragmentation using the Herfindahl index, i.e., a measure of the dispersion of the trading volume in a stock across the available trading platforms for this stock. Their data are very rich as they observe the limit order books of each trading platform for each stock. Hence, they can study the relationship between their index of market fragmentation and measures of depth at various price points in limit order books. They obtain two findings. First, the effect of market fragmentation on market liquidity is not monotonic. Moderate levels of market fragmentation are associated with an improvement in market liquidity but a too high level of market fragmentation is harmful for market liquidity. Second, they show that this pattern is more pronounced for incumbent exchanges. That is, an increase in market fragmentation for a stock initially improves the liquidity of the incumbent exchange for this stock but the latter deteriorates quickly as soon as market fragmentation exceeds a relatively low level. This finding suggests that investors who cannot access all trading platforms for a stock (who are “locked in” the incumbent market) might have been hurt.


# A central limit order book for European stocks

by the increase in market fragmentation in European markets. It again underscores that the effects of competition among trading platforms may depend on whether or not investors have easy access to all trading platforms.

Gresse (2011) applies a methodology similar to that used by Degryse et al.(2011) but for a different sample of European stocks (152 stocks constituents of the FTSE100, CAC40 and SBF120 indexes) and for a different period of time (September to November 2009). She finds a positive relationship between the level of market fragmentation for a stock and measures of market liquidity (consolidated across all trading platforms for this stock). Market fragmentation however seems to have a negative effect on the quoted depth of CAC40 stocks in Euronext. Moreover, there is no significant relationship between market fragmentation and liquidity for SBF120 stocks. These findings (as those in O’Hara and Ye (2011)) suggest that the effects of market fragmentation might depend on stock characteristics.

Last, two studies consider mergers between stock exchanges. When these mergers increase consolidation of order flow for a given stock, they can be used to shed light on the effect of such consolidation on liquidity. Arnold et al. (1999) consider mergers of regional stock exchanges in the U.S after the second world war and find that these mergers improved the liquidity of stocks traded on these exchanges. As noted by the authors, there are two possible interpretations for this finding. First, mergers between U.S. regional exchanges may have achieved economies of scale and the reduction in bid-ask spreads reflect the attendant cost savings for exchanges. Alternatively, these mergers may have helped regional exchanges to more efficiently compete for order flow with the NYSE. In this case, the empirical findings in Arnold et al. (1999) support the view that more efficient inter-market competition enhances market liquidity.

Pagano and Padilla (2006) and Nielsson (2009) study the formation of Euronext, resulting from the merger of the French, Belgian, Dutch and Portuguese stock exchanges in 2000 and 2003. Pagano and Padilla (2006) find a significant reduction in bid-ask spreads following the formation of Euronext and show that this reduction stems from cost savings and reduction in trading fees associated with the merger. These findings suggest that insofar as market fragmentation results in higher operating costs for exchanges, it may harm liquidity. Nielsson (2009) uses a larger sample of firms and shows that the gain in liquidity associated with Euronext formation has been unevenly allocated: these gains are concentrated among big firms and firms with large foreign exposure.

# Summary

To sum up, empirical analyses suggest that inter-market competition generally enhances consolidated market liquidity. However, this competition may become harmful if (i) it results in too high market fragmentation and (ii) it uselessly duplicates the cost of offering trading services to investors. Moreover, even though the entry of new trading platforms in Europe has increased consolidated liquidity, it may have reduced “local” liquidity (e.g., the liquidity of the incumbent market for a stock), as suggested by Degryse et al. (2011). For this reason, this entry may have been beneficial for investors who can easily trade in all trading venues for a security but not necessarily for those for which the cost of multimarket trading is too high.

9 This finding may explain why market participants are so split about the effects of MiFID on market liquidity (see the introduction).


A central limit order book for European stocks

# 3. Risk assessment

There are three risks associated with the present fragmentation of European equity markets. First, market fragmentation could lead to inefficient price discovery (mispricings). Indeed, the fragmentation of supply and demand for a stock among multiple securities can lead to different prices for the same stock in different trading venues and in some cases to even outright arbitrage opportunities. For instance, the best bid price for security XYZ in one market may match or exceed the best ask price in the other market. In such a situation, quotes in the two markets are said to be locked or crossed. In a well functioning market, locked and crossed quotes should not arise because they indicate that one buyer is willing to buy at a price at least equal to the price demanded by another seller. These two investors should therefore trade together.10

Second market fragmentation may prevent market participants from fully exploiting the benefit of thick market externalities (“network effects”). In presence of such externalities, investors’ welfare could be smaller when buy and sell trading interests are dispersed across multiple platforms because this fragmentation reduces the likelihood of finding a counterparty at an acceptable price. However, as explained previously, this problem exists only if it is costly for some market participants to access all competing platforms for a stock. Technological innovations should have reduced the costs of multi-market trading. Hence, thick market externalities should have a lesser role in today’s securities markets.

Third, market orders for a stock may not execute at the best possible price because it is difficult to enforce price priority across markets in a fragmented environment. This may have serious negative effects on the liquidity of the market for this stock. I now explain this point in more details.

As explained previously (see the discussion following Example 1), in presence of multiple trading venues, a broker often has several ways to route a market order. One would expect brokers to select the routing strategy that yields the best possible execution price for his clients. This may not be the case for several reasons, however. First, collecting information on limit orders posted in multiple markets is time consuming and costly. With the advent of electronic trading, the time cost of collecting information about offers in various markets has considerably decreased. However, trading platforms usually sell information on the quotes posted in their limit order books (directly or indirectly through data vendors such as Reuters or Bloomberg). Brokers or investors must therefore pay data fees to make fully informed routing decisions. In addition, in some cases, a platform may choose not to display all limit orders in its book.11 Obviously, this lack of transparency makes it more difficult for investors or their brokers to identify the optimal routing strategy at a given point in time.

10 Shkilko, Van Ness and Van Ness (2005) show that the ask and bid prices for stocks listed on Nasdaq and the NYSE (and traded on multiple markets) are locked or crossed 10% and 3.5% of the time, respectively. Storkenmaier and Wagener (2011) consider a sample of trades for FTSE100 stocks traded on the LSE, Chi-X, BATS and Turquoise. They find that in April/May 2010, quotes on these platforms are locked for about 6.4 minutes and crossed for 19.8 seconds, per day.

11 For instance, the NYSE started disseminating information on the limit orders posted behind the best quotes only in 2002.




A central limit order book for European stocks

In addition, brokers or investors will account for trading fees and clearing fees in making their routing decisions. In reality, trading platforms charge different trading fees. For instance, at the time of this report, BATS Europe and NYSE Arca Europe charge, respectively, a fee equal to 28 and 15 basis points of the total value traded to execute a market order.12 These fees are often small compared to the minimum difference between two prices in limit order books (the “tick size”) and therefore are unlikely to change the optimal routing strategy. However, if they are not entirely passed by brokers to their clients, they may bias brokers’ routing decision in favor of the market in which they pay the smallest fee.

Last, even though it is now easy to automate routing decisions (using “smart order routing systems”), executing one market order in multiple markets takes more time than placing this order in only one market. This is a source of concern as offers available in one market when the routing decision is made can vanish quickly, as explained in this quote from a representative of Fidelity (an asset management firm):13

“At Fidelity, we have no reason or incentive to by-pass readily accessible limit orders in any market where executions are certain and immediate. In seeking best execution of large orders, we seek the best overall execution, that is, best overall price. Walking the market up or down over several minutes or even seconds, if the ability to sweep the limit order book is denied, seriously impairs our ability to obtain the best execution for our funds. Often, liquidity at prices above or below the NBBO will fade away if we have to work our way, over the course of several seconds or minutes, above or below the NBBO. That fading away occurs as market professionals see us taking up liquidity at the prices nearer to the NBBO and then either compete with us for liquidity at the more distant prices or withdraw orders they have placed at those prices only to put them further away from what had been the NBBO.”

Hence, brokers or their clients might be willing to sacrifice best execution in terms of price in order to obtain a faster and more secure execution.

For all these reasons, brokers may not systematically seek to obtain the best possible execution price in making their routing decisions. Hence, market fragmentation can generate violations of price priority, i.e., cases in which market orders do not execute against the best posted quote in the market for a stock. Violations of price priority are sometimes called “trade-throughs” as when they occur, everything is as if market orders were “trading through” the best price in the market. Trade-throughs are problematic for several reasons.

1. Trade-throughs are a source of volatility. For instance, consider Example 1 again and suppose that the fundamental value of stock XYZ is €42.945 (the mid-point between the best ask price and the best price in the market for stock XYZ). The buy market order for 900 shares will trigger a deviation from this fundamental value equal to 42.964 – 42.945 = 0.019 if the order only executes in NSC. If, instead, the order is optimally split between NSC and BATS, this deviation is smaller and equal to 0.05. Thus, suboptimal routing decisions amplify price movements due to market illiquidity.

12 See http://www.batstrading.co.uk/resources/participant_resources/BATSEuro_Pricing.pdf

13 Letter from Eric D. Roiter, Senior Vice President and Gen. Counsel, Fidelity Mgmt. &#x26; Research Co., to Jonathan Katz, Sec’y, SEC (June 22, 2004), available at http://www.sec.gov/rules/proposed/s71004/sdesano072204.pdf.




A central limit order book for European stocks

2. Trade-throughs reduce the likelihood of execution for investors’ limit orders even if their orders are aggressively priced. For instance, in Example 1, the sell limit order at €42.95 in BATS has a smaller chance of getting filled if a fraction of brokers do not pay sufficient attention to the quotes in BATS. This is a concern since there are opportunity costs and sometimes real costs for investors with unfilled limit orders.14 Worse, trade-throughs discourage investors from competing in prices, i.e., to post aggressively priced limit orders. For instance, in Example 1, the investor with a sell limit order at €42.96 has less incentive to match or even undercut the sell limit order at €42.95 in BATS if he anticipates that some brokers will not give priority to BATS, even though this platform displays a better price. As a result, trade-throughs soften competition among investors submitting limit orders and thereby impair market liquidity.15

3. Trade-throughs act as a barrier to entry (see Foucault and Menkveld (2008)). Indeed, in order to attract market orders and obtain trading revenues, a new platform (the “entrant”) must first attract competitive limit orders since market orders are matched with limit orders. However, investors have an incentive to post limit orders in the new platform only if they expect a sufficiently high likelihood of execution. As I just explained, this will not be the case if limit orders in the entrant platform are not protected against trade-throughs.

Ende and Lutat (2010) estimate the frequency of trade-throughs in the constituent stocks of the Euro Stoxx 50 index traded in eight European markets over 20 trading days in 2007 and 2008.16 Trade-throughs occur for 12% of the trades in their sample. This situation could just be transitory and trade-throughs might disappear as market participants equip themselves to trade in a multimarket setting (e.g., by using smart order routing technologies).

# 4. Options

There are three options to alleviate the risks associated with the market fragmentation of European equity markets.

- Option 1: Mandating a consolidated limit order book (a CLOB) for each European stock. A decision will have to be made in this case about how stocks are allocated to different platforms. One can imagine at least two allocation schemes: (i) trading platforms compete for listings and the trading platform on which a stock is listed operates the CLOB for this stock; (ii) trading platforms bid periodically (say every 5 years) to have the right to trade a stock, which can be listed elsewhere and the proceeds of this auction go to (a) the issuing firm or (b) the exchange listing the firm. Another decision must be made in this case about whether OTC trading would be allowed. A strict version of Option 1 would ban OTC trading (which would require suppressing the possibility for brokers-dealers to “internalize” orders from their clients, i.e., to execute these trades in-house).

14 For instance, to hedge a position in one security, an investor may sell another security using a limit order. If this limit order does not execute, the investor’s hedge will be ineffective and the investors’ exposure to risk higher than desired.

15 Foucault and Menkveld (2008) provide evidence consistent with this possibility.

16 These markets are Xetra Dax, Xetra Stoxx, Euronext, Bolsa Italiana Milan, Bolsa de Madrid, SWX Europe, Chi-X and the Helsinki Stock Exchange.




A central limit order book for European stocks

Option 2: Continuing to operate under the current regime but with a market structure that strengthens investors’ ability to readily access competing trading venues. To this end, more real time information on posted limit orders, transaction prices, and traded quantities in competing trading venues for a stock is needed. For the moment, there is no single provider of consolidated information on limit order books (pre trade information), transaction prices and volume (post trade information) in Europe. As a result, the costs of data collection are high. For instance, 64% of the respondents to the survey of the CFA Institute on the impact of MiFID consider that the cost of data access has increased with MiFID and 65% estimate that a mandated consolidated tape would be beneficial.17

Another problem is that there are multiple clearinghouses (central clearing counterparties or CCPs) in Europe and trading platforms often use the service of a single CCP.18 Hence, clearing fees vary across platforms and this heterogeneity makes it more difficult for investors to determine how to best route their orders. Moreover, when investors trade on a platform, they have no choice but using the CCP chosen by this platform. This endows CCPs with significant pricing power in the choice of their fees. One way to solve the first problem would be to have a single CCP for all competing platforms as in U.S. equity markets. This solution however has the drawback of giving monopoly power to one CCP in the provision of clearing services. Alternatively, one can have multiple CCPs for each platform and let investors choose their preferred CCP. In this way, investors could use the same CCP independently of the platform on which they conduct their trade for a specific security.19

Option 3: Same as Option 2 but with stronger priority rules across markets. In particular, one rule could prevent a trading venue for a stock from displaying a bid (ask) price higher (lower) or equal to the ask (bid) price on another venue (a “no crossed/locked market” rule). Moreover, a “no-trade through” rule could be used to preclude trading in one trading venue at a price worse than in another trading venue and to protect limit orders from violations of price priority. Investors’ ability to readily access all trading platforms is a pre requisite for the enforcement of these rules. Hence Option 3 cannot be considered independently of Option 2. It is just a stronger version of Option 2.

Several decisions must be made with regard to the exact design of the no trade-through rule. Regulation must first specify whether this rule should apply to best quotes only or all quotes in a limit order book. Consider again our example in which an investor submits a buy market order for 900 shares. If the trade-through rule applies only to best quotes, executing this market order entirely on BATS Europe complies with the trade-through rule but it does not yield the best possible average execution price for the investor. In contrast, if the no trade-through rule applies to all quotes in both markets then the market order must execute in such a way that it yields the best possible average execution price for the investor. Hence, protecting all quotes in

17 A consolidated tape is a system that aggregates and disseminates real-time information on transaction prices and volume for a stock when it trades on multiple platforms.

18 When a trade takes place, a Central Clearing Counterparty (CCP) interposes itself between the buyer and the seller. If the buyer (seller) defaults to its obligations, the CCP will substitute to the buyer (seller) so that the transaction can be completed. For this insurance, buyers and sellers pay a fee to the CCP.

19 This approach is called «interoperability » and has been first implemented by BATS Europe in January 2012.




A central limit order book for European stocks

Limit order books from trade-throughs makes more sense but this approach might be technically difficult and costly to implement.

A second issue is whether the trade-through rule applies to quotes cum fees or just quotes. As explained previously, trading platforms charge different fees on market orders (so called “take” fees). If brokers pass these fees to their clients, the final price received or paid by an investor depends on these fees and the trade-through rule should therefore be based on quotes adjusted for take fees to be economically meaningful.

A last issue is the enforcement of the no trade-through rule. One possibility is to require platforms to reroute market orders to the platform posting the best price at any point in time. Another possibility is to require brokers to avoid trade-throughs as part of their duty of best execution.

Interestingly, all these approaches have been discussed for long in the U.S. In the 70s, trading in stocks listed on the NYSE was primarily taking place on the NYSE. Yet, there were also trades in these stocks on regional exchanges (Boston, Philadelphia etc…) and the OTC market. The Congress was concerned that this situation could lead to inefficiencies. It therefore mandated the SEC to create a National Market System (NMS) in 1975. The SEC initially proposed to consolidate all limit orders for a stock in a single file, where price priority and time priority (for limit orders entered at the same price) would be enforced. 20 This proposal became known as the Central Limit Order Book approach and is similar to Option 1.

The SEC faced strong opposition to this proposal from exchanges and market-makers and eventually chose a more decentralized approach to build a National Market System. First, to facilitate access to information on quotes and trades, it created the Consolidated Quote System (CQS) to disseminate information on best ask and bid prices in each trading venue for a stock (“pre trade information”) and the Consolidated Tape System (CTS) to disseminate information on transaction prices (“post trade information”). Moreover, under the prodding of the SEC, several exchanges launched the Intermarket Trading System (ITS). The ITS provided a system to route market orders received by an exchange to another exchange, in case the latter offers a better price. In particular, exchanges participating to this system agreed to a no trade-through rule, prohibiting a participant from trading at a price inferior to that available in another market. Thus, instead of creating a single central limit order book for each stock, the SEC authorized the co-existence of multiple trading venues for a single stock, relying on the dissemination of real-time information and inter-market linkages to integrate these markets.

This approach, which corresponds to Option 3, has been strengthened in 2006, with a new set of trading rules known as RegNMS. 21 One pillar of RegNMS is the so called “Order Protection Rule.” According to this rule, a trading platform that receives a marketable order must reroute this order to the platform posting the best bid or offer price (depending on whether the order is a sell or a buy order) at the time the order is received. Thus, the best posted quotes in the market are protected from trade-throughs (but not the quotes behind the best quotes). 22 The Order protection Rule is more stringent than the no trade through rule set forth in the ITS system. For instance, it applies to Nasdaq listed stocks, which were not covered by the no trade-through rule in the ITS system.

19


A central limit order book for European stocks

The goal of the Order Protection Rule is to encourage investors to post limit orders by raising the chance that they will attract market orders if they post the best price, as emphasized in its 2005 release on Regulation NMS (p. 36): “Price protection encourages the display of limit orders by increasing the likelihood that they will receive an execution in a timely manner and helping preserve investors’ expectations that their orders will be executed when they represent the best displayed quotation.”

# 5. Costs, risks and benefits

The costs and benefits of the options described in Section 4 are discussed in this section.

# Option 1.

Option 1 has one benefit: it suppresses market fragmentation and the risks highlighted in Section 3 with the current market structure. This should result in an improvement in market quality if market fragmentation is harmful for liquidity. However, this solution has also several major drawbacks. First, as explained in section 2, it is far from clear that the coexistence of multiple platforms is harmful for investors. Existing empirical studies have not detected such an effect (and often find that market fragmentation improves market liquidity) and recent theories find that a CLOB could in fact reduce market liquidity. Second, a CLOB effectively endows one platform with a monopoly position, at least for some time. Hence, unless trading fees are regulated, there is a risk that this trading platform charges high trading fees at investors’ expense. Another drawback is that this solution would constitute a major change relative to the current environment with possibly unexpected effects.

# Option 2.

The benefit of Option 2 is that it retains the benefits associated with intermarket competition (such as lower trading fees, more innovative platforms etc; see Section 2) while modifying the current market structure to lower the costs of trading in a multi-market environment for investors. There are two types of risks associated with this option. First, the infrastructure required for disseminating consolidated information in real time must be developed. This is costly. Second, and maybe more important, the price of real time consolidated information must be low as otherwise some investors will choose not to acquire this information. This price depends both on the cost of disseminating market data (which needs to be assessed) and the organization of the market for real time information. If this market is not sufficiently competitive then there is a risk that the price of market data will be too high. This depends in part on trading platforms. Indeed, price and trade data are first available to platforms which can then sell this information to data vendors. If platforms price their information dearly then data vendors will pass this cost to their clients. Hence, the regulator may require platforms to disseminate free of charge (or at cost) trade and price information. This solution is likely to be very controversial since some exchanges obtain large revenues from the sale of information.

# Option 3.

Option 3 attempts to retain the benefits of inter-market competition (as Option 2) while mitigating potential harmful effects of market fragmentation by linking markets together. Hence, the ultimate goal of Option 3 would be to create a virtual CLOB (as in Option 1) but with multiple platforms contributing to the CLOB. As explained previously, an important step to create such a virtual CLOB would be to impose a no crossed-locked market rule and a no trade through rule. The exact design of the rules is very important. For instance, the trade-through rule should apply to quotes cum fees as otherwise it could distort competition among platforms. Indeed, if the trade-through rule applies to raw quotes, then a platform can attract market orders even if it charges non-competitive take fees as long as it displays a tight bid-ask.




A central limit order book for European stocks

spread. In this case, the trade-through rule could allow platforms to enjoy more pricing power at the expense of investors. Another problem of the no trade through rule is that it forces investors to base their routing decisions on prices only. In reality, there are other dimensions than prices to best execution. For instance, investors might be willing to trade at a worse price if they can get faster execution, something that is no possible under a strict version of a no-trade-through rule.

This discussion shows that choices between these options will affect different types of businesses in the financial industry: (i) trading platforms’ operators, (ii) brokers, (iii) asset managers, (iv) proprietary trading firms, (vi) central counterparties, (vii) data vendors, and (ix) firms selling technologies helping investors to navigate in fragmented markets (e.g., firms developing smart routers or tools to consolidate quotes in various markets).

# 6. Future

Section 3 describes the risks associated with the current fragmentation of trading in European equity markets. It is possible that these risks will disappear even in the absence of regulatory actions for several reasons. First, arbitrageurs have incentives to integrate markets (e.g., a crossed market is a profit opportunity for an arbitrageur). Moreover, it is in investors’ self-interest to avoid trade-throughs since this results in smaller trading costs for them. Hence, it is possible that inefficiencies with the current environment (e.g., the trade-throughs documented in Ende and Lutat (2011)) will progressively disappear.23 In support of this view, Battalio, Hatsch and Jennings (2004) show that the frequency of trade-throughs in US options markets was high when these markets started competing together in 1999. However, this fraction declined quickly afterwards without the need of regulatory intervention. Similarly, Storkenmaier and Wagenere (2011) find that the percentage of trade-throughs as a fraction of the total number of trades for FTSE 100 stocks declined by about 2% from 2009 to 2010.

It is also possible that private operators will see a business opportunity in providing market participants with a consolidated tape and information on offers posted in multiple limit order books. In this case, there is no need of a regulatory impetus for the provision of this information.

In all these cases, participants will create the virtual consolidated limit order book that Options 2 and 3 described in Section 4 aim at creating.

The level of market fragmentation is now quite high in Europe. It may decline however with future mergers between existing markets. Indeed, although competition between platforms has benefits (as explained in section 2), it is not clear why many platforms are needed to achieve these benefits. There is therefore a possibility of consolidation in the provision of trading services in the next decade.

Another potential change is in the market for listings. For the moment competition among platforms is a competition for the provision of trading services. There is much less competition

When the SEC strengthened the no trade-through rule in the U.S., many commenters argued that this was useless as there were fewer trade-throughs in Nasdaq stocks (which were not covered by the no trade-through rule before RegNMS) than NYSE stocks (which were covered by a no-trade-through rule). See “Regulation NMS,” Release No. 34-51808; File No. S7-10-04, SEC (2006).

21


A central limit order book for European stocks

for the provision of listing services to firms. Indeed, European firms keep being listed mainly on the main exchange in their country of origin and there has been no attempt by Multilateral Trading Platforms (MTFs) to attract listings from these incumbent markets (e.g., by offering lower listing fees to firms). The success of MTFs suggests that attracting listings is not critical to build up a significant market share in the provision of trading services. Hence, in the future, one could see an unbundling of the provision of trading services on the one hand and listing services on the other hand.

# 7. Summary

There are two ways to implement a central limit order book. The “hard” way consists in mandating consolidation of all trades in a stock on a single platform operating a limit order book. The “soft” way consists in creating a virtual central limit order book by linking competing platforms together in such a way that ultimately trades happen as if all limit orders for a stock were consolidated in a single limit order book.

The first approach is risky for a variety of reasons and there is no evidence indicating that it would make investors better off.

The advantage of the second approach is that it retains the benefits of inter-market competition (low trading fees, innovation in trading services etc…) while mitigating the risks associated with market fragmentation. Hence, my recommendation is to follow this second approach.

This approach requires facilitating access to market data for investors, lowering the cost of multi-market trading (in particular those associated with clearing and settlement) and setting forth rules that guarantee that at least price priority is enforced across platforms (i.e., Option 3). These changes to the current environment for European equity markets are pre-requisites to create a central limit order book with “multiple points of entry.” It is possible that market forces will lead market participants to develop tools and take actions that enable them to seamlessly trade in the European equity markets as if offers posted in these markets were all consolidated in a single central limit order book. If not, regulatory intervention will be needed to give the impetus required for these changes.

22


# A central limit order book for European stocks

# References

- Admati A., and P. Pfleiderer, (1988) “A theory of intraday patterns: volume and price variability” Review of Financial Studies 1, 3-40.
- Arnold, T., Hersch, P., Mulhering, H. and Netter, J. (1999) “Merging markets”, Journal of Finance 49, 1083-1107.
- Battalio R., Hatch B., and Jennings R.H., (2004) “Towards a National Market System for U.S. exchange-listed equity options”, Journal of Finance 54, 933–962.
- Battalio R., (1997) “Third Market Broker-Dealers: Cost Competitors or Cream Skimmers?”, Journal of Finance 52, 341-351.
- Biais B., Bisière C., and Spatt C., (2010) “Imperfect Competition in Financial Markets: An Empirical Study of Island and Nasdaq”, Management Science 5, 2237-2250.
- Biais, B., Martimort D., and Rochet, J.C. (2000), "Competing Mechanisms in a Common Value Environment", Econometrica 68, 799-837.
- Boehmer B., and Boehmer E., (2003) “Trading your neighbor’s ETFs: Competition or fragmentation”, Journal of Banking and Finance 27, 1667–1703.
- Colby R. and Sirri, E., (2010) “Consolidation and competition in the US equity markets”, Capital Markets Law Journal, 5, 169-196.
- Chowdhry B., and Nanda V., (1991) “Multimarket trading and market liquidity”, Review of Financial Studies 4, 483–511.
- Colliard J.E, and Foucault T., (2011), “Trading fees and efficiency in limit order markets”, CEPR Discussion Paper Series, n°8395. Latest version available at: http://www.hec.fr/foucault.
- DeFontnouvelle P., Fishe RPH., and Harris JF., (2003) “The behavior of bid-ask spreads and volume in options markets during the competition for listings in 1999”, Journal of Finance 58, 2437–2464.
- Degryse H., deJong, F., and V. Van Kervel, (2011) “The impact of dark trading and visible fragmentation on market quality”, CEPR discussion paper 8630.
- Ende B. and M. Lutat, (2011) “Trade-throughs in European Cross-traded Equities After Transaction Costs– Empirical Evidence for the EURO STOXX 50”, Working paper, Goethe Universität.
- Foucault T., and Menkveld AJ., (2008) “Competition for Order Flow and Smart Order Routing Systems”, Journal of Finance, 63, 119-158.
- Foucault T., and Gehrig T., (2008) “Stock Price Informativeness, Cross-Listings and Investment Decisions”, Journal of Financial Economics, 88, 146-168.


# A central limit order book for European stocks

Glosten L., (1994) “Is the electronic order book inevitable?”, Journal of Finance 49, 1127–1161.

Gresse C., (2011), “Effects of the competition between multiple trading platforms on market liquidity: evidence from the MiFID experience”, working paper, Université Paris-Dauphine.

Nielsson, U., (2009), “Stock exchange merger and liquidity: The case of Euronext”, Journal of Financial Markets, 12, 229-267.

O’Hara M., and Ye M., (2011) “Is market fragmentation harming market quality”, Journal of Financial Economics, 100, 459-474.

Pagano, M. and Padilla J. (2006) “Effects of stock exchange integration: The Euronext evidence,” Working paper, University of Naples, Frederico II.

Pagano M., (1989) “Trading volume and asset liquidity”, Quarterly Journal of Economics 104, 255–274.

Peake J., (2007) “Entropy and the National Market System”, Brooklyn Journal of Corporate, Financial &#x26; Commercial Law, 1, 301-315.

SEC (2010), Concept Release on Equity Market Structure, Release No. 34-61358; File No. S7-02-10.

SEC (2006) Regulation NMS,” Release No. 34-51808; File No. S7-10-04, SEC (2006).

Shkilko Y., Van Ness B., and R. Van Ness, (2008) “Locked and crossed markets on Nasdaq and NYSE”, Journal of Financial Markets 11, 308-337.

Storkenmaier A. and Wagener M. (2011) “Do we need a European National Market System?”, working paper, available at http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1760778



# A central limit order book for European stocks

© Crown copyright 2012

You may re-use this information (not including logos) free of charge in any format or medium, under the terms of the Open Government Licence. Visit www.nationalarchives.gov.uk/doc/open-government-licence write to the information Policy Team, The National Archives, Kew, London TW9 4DU, or email: psi@nationalarchives.gsi.gov.uk

Foresight

1 Victoria Street

London SW1H 0ET

www.foresight.gov.uk

URN: 12/1074

25

