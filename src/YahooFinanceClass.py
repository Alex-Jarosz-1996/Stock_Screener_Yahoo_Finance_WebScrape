class StockClass:
    def __init__(self):
        # stock price metrics
        self.ticker          = None
        self.price           = None
        self.marketCap       = None
        self.numSharesAvail  = None
        self.yearlyLowPrice  = None
        self.yearlyHighPrice = None
        self.fiftyDayMA      = None
        self.twoHundredDayMA = None

        # value metrics
        self.acquirersMultiple     = None
        self.evToRev               = None
        self.evToEBITDA            = None
        self.enterpriseValue       = None
        self.peRatioTrail          = None
        self.peRatioForward        = None
        self.priceToSales          = None
        self.priceToBook           = None
        self.bookValPerShare       = None
        self.cashPerShare          = None
        self.cashToMarketCap       = None
        self.cashToDebt            = None
        self.currentRatio          = None
        self.debtToMarketCap       = None
        self.debtToEquityRatio     = None
        self.eps                   = None
        self.ebitdaPerShare        = None
        self.grossProfitPerShare   = None
        self.netIncomePerShare     = None
        self.netIncomeMarginRatio  = None
        self.revenuePerShare       = None
        self.evToOperatingCashFlow = None
        self.ocfToRevenueRatio     = None
        self.lfcfToMarketCap       = None
        self.lfcfPerShare          = None
        self.ocfToMarketCap        = None
        self.ocfPerShare           = None

        # dividend metrics
        self.exDivDate     = None
        self.payoutRatio   = None
        self.forwDivYield  = None
        self.forwDivRate   = None
        self.trailDivYield = None
        self.trailDivRate  = None

        # balance sheet metrics
        self.cash           = None
        self.debt           = None
        self.returnOnAssets = None
        self.returnOnEquity = None
        
        # income related
        self.earningsGrowth  = None
        self.ebitda          = None
        self.grossProfit     = None
        self.netIncome       = None
        self.operatingMargin = None
        self.profitMargin    = None
        self.revenue         = None
        self.revenueGrowth   = None

        # cash flow related
        self.lfcf = None
        self.ocf  = None

    def __repr__(self, obj):
        return obj

    def __str__(self, obj):
        return obj

