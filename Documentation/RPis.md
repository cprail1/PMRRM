There are several Raspberry Pi's on the layout.

At Zion East, there's one that's providing a temporary soft panel.  It can be accessed as `ZionE-RPi.local.`

In the gallery, there are several RPis driving the operator displays.  These all run the same image.  They advertise as `operator-display.local.`.  It's not clear how the multiple RPi's share that mDNS name.

There's also an RPi at Alhambra.  It's not clear whether it advertises or not.  it might be `RPi-JMRI.local.`

The Windows `mDNS Discovery` app from the Microsoft App Store might be able to resolve names on the network; Google cautions to "Make sure your Windows Network Profile is set to "Private" so your firewall doesn't block local multicast traffic."

