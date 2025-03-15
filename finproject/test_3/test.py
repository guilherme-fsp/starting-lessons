import yfinance as yf

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")  # Adiciona ".SA" para ações da B3
    info = ticker.info
    return info

def search_data():
    user_text = input("Digite o código B3: ").strip().upper()  # Exemplo: BBAS3
    dados = fetch_data(user_text)

    if not dados:
        print("Nenhum dado encontrado.")
        return

    user_select = input('Digite os parâmetros desejados separados por vírgula (ou pressione Enter para parâmetros básicos): ').strip()

    if not user_select:
        # Parâmetros básicos padrão
        
        chaves_desejadas = {'address1': 'endereço', 'address2': 'endereço2', 'city' : 'endereço3', 'state' : 'endereço4', 'country' : 'endereço5', 'phone' : 'telefone', 'website' : 'site', 'website': 'link', 'industry' : 'setor', 'industryKey' : 'setor chave'}, # 'industryDisp', 'sector', 'sectorKey', 'sectorDisp', 'longBusinessSummary', 'companyOfficers', 'regularMarketVolume', 'averageVolume', 'volume', 'forwardPE', 'trailingPE', 'regularMarketDayHigh', 'fiveYearAvgDividendYield', 'payoutRatio', 'exDividendDate', 'dividendYield', 'dividendRate', 'regularMarketDayLow', 'regularMarketOpen', 'regularMarketPreviousClose', 'dayHigh', 'dayLow', 'open', 'previousClose', 'priceHint', 'maxAge', 'governanceEpochDate', 'overallRisk', 'shareHolderRightsRisk', 'compensationRisk', 'boardRisk', 'auditRisk', 'trailingPegRatio', 'financialCurrency', 'operatingMargins', 'revenueGrowth', 'operatingCashflow', 'returnOnEquity', 'returnOnAssets', 'revenuePerShare', 'totalRevenue', 'totalDebt', 'totalCashPerShare', 'totalCash', 'numberOfAnalystOpinions', 'recommendationKey', 'recommendationMean', 'targetMedianPrice', 'targetMeanPrice', 'targetLowPrice', 'targetHighPrice', 'currentPrice', 'gmtOffSetMilliseconds', 'messageBoardId', 'uuid', 'timeZoneShortName', 'timeZoneFullName', 'firstTradeDateEpochUtc', 'longName', 'shortName', 'underlyingSymbol', 'symbol', 'quoteType', 'exchange', 'lastDividendDate', 'lastDividendValue', 'SandP52WeekChange', '52WeekChange', 'enterpriseToRevenue', 'lastSplitDate', 'lastSplitFactor', 'forwardEps', 'trailingEps', 'netIncomeToCommon', 'earningsQuarterlyGrowth', 'mostRecentQuarter', 'nextFiscalYearEnd', 'lastFiscalYearEnd', 'priceToBook', 'bookValue', 'impliedSharesOutstanding', 'heldPercentInstitutions', 'heldPercentInsiders', 'sharesOutstanding', 'floatShares', 'profitMargins', 'enterpriseValue', 'currency', 'trailingAnnualDividendYield', 'trailingAnnualDividendRate', 'twoHundredDayAverage', 'fiftyDayAverage', 'priceToSalesTrailing12Months', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'marketCap', 'ask', 'bid', 'averageDailyVolume10Day', 'averageVolume10days'}
        
        
    else:
        # Divide a entrada do usuário em uma lista de chaves
        chaves_desejadas = [param.strip() for param in user_select.split(',')]

    print("\nDados coletados:")
    for chave in chaves_desejadas:
        valor = dados.get(chave, 'N/A')
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    search_data()
