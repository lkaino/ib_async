from ib_async import Contract, IB, MarketOrder, OrderStatus, Trade


def test_tif_preset_warning_10349_preserves_live_order_status():
    ib = IB()
    wrapper = ib.wrapper
    order = MarketOrder("BUY", 37, orderId=112622)
    trade = Trade(Contract(symbol="SRZN"), order, OrderStatus(orderId=112622, status=OrderStatus.Submitted))
    wrapper.trades[(wrapper.clientId, order.orderId)] = trade

    wrapper.error(order.orderId, 10349, "Order TIF was set to GTC based on order preset.", "")

    assert trade.orderStatus.status == OrderStatus.Submitted
    assert not trade.isDone()
