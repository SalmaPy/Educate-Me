from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6718188580:AAG8i9F7j6YD2XnvN-_GgmKs7NfWiii2mdk'
BOT_USERNAME: Final = '@Palestine_lovers_bot'

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('مرحبًا! تعال لنستكشف سويًا تاريخ فلسطين خلال الفترة من عام 1981 إلى عام 1995 يمكنك التعرف على اهم الشخصيات والاحداث والشهداء في هذه الفترة من خلال الضغط على اسم القائمة المطلوبة ')

async def characters_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('خلال هذه الفترة (1981-1985)، ظهرت عدة شخصيات بارزة في فلسطين والمنطقة المحيطة بها. من بين هؤلاء الشخصيات : '
                                    ' 1- ياسر عرفات: كان زعيمًا بارزًا في الحركة الوطنية الفلسطينية، وشغل مناصب رئاسية في منظمة التحرير الفلسطينية. كان يُعتبر رمزًا للنضال الفلسطيني ضد الاحتلال الإسرائيلي. '
                                    ' 2- أنور السادات: كان الرئيس المصري في هذه الفترة، وقاد مصر في عملية السلام مع الاحتلال، مما أدى في النهاية إلى اتفاقية كامب ديفيد واتفاقية السلام المصرية الإسرائيلية. '
                                    ' 3-  مناضلون فلسطينيون بارزون: مثل جورج حبش، الذي كان قائدًا عسكريًا لمنظمة التحرير الفلسطينية، ولعب دورًا هامًا في النضال الفلسطيني ضد الاحتلال الإسرائيلي. '
                                    ' 4- يتسحاك رابين: كان رابين رئيسًا الوزراء للكيان المحتل في هذه الفترة، وشارك في التفاوض مع الفلسطينيين والمصريين من أجل تحقيق السلام.' 
                                    ' 5- حافظ الأسد: كان الرئيس السوري في ذلك الوقت، ولعب دورًا في تشكيل السياسة الإقليمية والتفاوض مع الاحتلال الاسرائيلي والمجتمع الدولي. '
                                    ' هذه بعض الشخصيات البارزة في الساحة الفلسطينية والمنطقة المحيطة بها خلال الفترة المطلوبة. ')

async def news_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' خلال الفترة من عام 1981 إلى 1985، شهدت فلسطين العديد من الأحداث الهامة. هنا بعض الأحداث البارزة خلال تلك الفترة: '
                                    ' 1- مجازر صبرا وشاتيلا (1982): وقعت هذه المجازر في مخيمي صبرا وشاتيلا في بيروت، لبنان، حيث قتل آلاف الفلسطينيين المدنيين على يد مجموعة مسلحة مسيحية فلسطينية، في أعقاب الاجتياح الإسرائيلي للبنان '
                                    ' 2- اتفاقية الطائف (1983): وُقعت هذه الاتفاقية في لبنان، وقد أنهت الحرب الأهلية اللبنانية بين الطوائف المسيحية والمسلمة. لم تُنهِ الاتفاقية النزاعات الفلسطينية، لكنها أعطت بعض الاستقرار للبلاد. '
                                    ' 3- الانسحاب الإسرائيلي من جنوب لبنان (1985): انسحبت إسرائيل جزئياً من لبنان، بعد عملية "خواعين النجوم" التي نفذتها قوات الدفاع الإسرائيلية في 1985. '
                                    ' 4- تأسيس حركة حماس (1987): بدأت حركة حماس كفرع من جماعة الإخوان المسلمين في فلسطين، واشتهرت بمواجهتها للسلطة الفلسطينية والاحتلال الإسرائيلي. '
                                    ' هذه الأحداث تمثل بعضًا من الأحداث الرئيسية التي وقعت في فلسطين والمنطقة المحيطة بها خلال الفترة التي طلبتها. ')

async def shuhada_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' خلال الفترة من عام 1981 إلى 1985، فإن الشهداء الفلسطينيين الذين استشهدوا كانوا عددهم كبيرًا، ويتضمنون مدنيين ومقاتلين. بسبب الاحتلال الإسرائيلي والصراعات الدائرة في المنطقة، فإن العديد من الفلسطينيين فقدوا حياتهم. من الصعب تحديد أسماء جميع الشهداء بدقة في تلك الفترة، ولكن يمكن تذكير بعض الشهداء البارزين، مثل: '
                                    ' 1- الشهداء في مجازر صبرا وشاتيلا (1982): ضحايا الهجوم على مخيمي صبرا وشاتيلا في بيروت، حيث قتل آلاف الفلسطينيين المدنيين على يد ميليشيات مسيحية متحالفة مع إسرائيل. '
                                    ' 2- المقاتلين الفلسطينيين: خلال النضال ضد الاحتلال الإسرائيلي والمشاركة في مختلف العمليات العسكرية والمقاومة، فقد العديد من المقاتلين الفلسطينيين حياتهم. '
                                    ' 3- المدنيين الفلسطينيين: كان هناك العديد من المدنيين الفلسطينيين الذين فقدوا حياتهم جراء الاقتتال الدائر في لبنان والنزاعات الفلسطينية الإسرائيلية. '
                                    ' هذه بعض الأمثلة على الشهداء الفلسطينيين الذين استشهدوا في تلك الفترة، ولكن القائمة ليست شاملة وتحتاج إلى مزيد من البحث لتحديد الأسماء بدقة. ')

async def characters2_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' خلال الفترة من عام 1986 إلى 1990، ظهرت العديد من الشخصيات البارزة التي لعبت أدواراً مهمة في الصراع الفلسطيني الإسرائيلي والأحداث السياسية في المنطقة. بعض الشخصيات البارزة في ذلك الوقت تشمل: '
                                    ' 1- ياسر عرفات: كان زعيمًا لمنظمة التحرير الفلسطينية (منظمة التحرير)، ولعب دورًا مهمًا في المفاوضات مع الكيان المحتل وفي توجيه الانتفاضة الفلسطينية الأولى. '
                                    ' 2- شمعون بيريز: كان رئيسًا للكيان المحتل في تلك الفترة، وقاد جهود السلام مع الفلسطينيين، بما في ذلك مشاركته في مفاوضات أوسلو. '
                                    ' 3- محمود عباس (أبو مازن):  شغل مناصب مهمة في منظمة التحرير الفلسطينية وكان جزءًا من الفريق الفلسطيني في مفاوضات أوسلو.'
                                    ' 4- يتشاك رابين: كان وزير الدفاع في الكيان المحتل، وقاد العملية التي أدت إلى توقيع اتفاقية أوسلو. '
                                    ' 5- محمود درويش: كان شاعرًا فلسطينيًا بارزًا، وأحد أبرز الأدباء والشخصيات الثقافية في الفترة الحديثة للتاريخ الفلسطيني. '
                                    ' هذه بعض الشخصيات البارزة في الفترة من عام 1986 إلى 1990، التي لها تأثير كبير على الأحداث والتطورات في فلسطين والمنطقة المحيطة بها. ')

async def news2_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' خلال الفترة من عام 1986 إلى 1990، شهدت فلسطين والمنطقة المحيطة بها العديد من الأحداث الهامة، من بينها:'
                                    ' 1- انتفاضة الشباب الفلسطينية (انتفاضة الحجارة) (1987-1993): بدأت هذه الانتفاضة في ديسمبر 1987، عندما قامت مجموعات من الشبان الفلسطينيين برمي الحجارة على الجنود الإسرائيليين في قطاع غزة والضفة الغربية، في رد فعل على الاحتلال الإسرائيلي. كانت هذه الانتفاضة نقطة تحول مهمة في الصراع الفلسطيني الإسرائيلي. '
                                    ' 2- تأسيس منظمة التحرير الفلسطينية (مجلس الأمن الوطني): في نوفمبر 1988، أعلنت منظمة التحرير الفلسطينية استقلال دولة فلسطين وقامت بتشكيل "مجلس الأمن الوطني" لإدارة شؤون الدولة.'
                                    ' هذه الأحداث تمثل بعضًا من النقاط المهمة خلال الفترة من 1986 إلى 1990 في فلسطين والمنطقة المحيطة بها، وقد كانت لها تأثير كبير على الصراع الفلسطيني الإسرائيلي والسياسة الإقليمية. ')

async def shuhada2_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' خلال الفترة من عام 1986 إلى 1990، فقد العديد من الفلسطينيين حياتهم في مختلف الأحداث والمواجهات. من الصعب تحديد الأسماء بدقة، لكن بعض الشهداء الفلسطينيين الذين استشهدوا في تلك الفترة شملوا:'
                                    ' 1- شهداء الانتفاضة الفلسطينية (انتفاضة الحجارة): تم قتل العديد من الفلسطينيين خلال المواجهات مع القوات الإسرائيلية خلال فترة الانتفاضة التي بدأت في عام 1987.'
                                    ' 2- شهداء المواجهات الداخلية في الضفة الغربية وقطاع غزة: كانت هناك أيضًا مواجهات داخلية بين الفلسطينيين وبين جماعات مسلحة داخلية في تلك الفترة، مما أدى إلى خسارة حياة العديد من الفلسطينيين. '
                                    ' 3- شهداء العمليات العسكرية والمواجهات مع الكيان المحتل : تواصلت العمليات العسكرية والمواجهات بين الفلسطينيين والقوات الإسرائيلية خلال هذه الفترة، وتسببت في فقدان حياة العديد من الفلسطينيين. '
                                    ' تلك الفترة كانت حافلة بالصراعات والمواجهات، مما أدى إلى استشهاد العديد من الفلسطينيين، سواء كانوا مدنيين أو مقاتلين، ولكن من الصعب تحديد الأسماء بدقة بسبب تعقيدات الوضع السياسي والأمني في تلك الفترة. ')

async def characters3_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' خلال الفترة من عام 1991 إلى 1995، ظهرت العديد من الشخصيات البارزة التي كان لها دور كبير في الأحداث السياسية والتطورات في فلسطين والمنطقة المحيطة بها. بعض هذه الشخصيات تشمل:'
                                    '  1-  ياسر عرفات: كان زعيمًا بارزًا في منظمة التحرير الفلسطينية، ولعب دورًا هامًا في توقيع اتفاقية أوسلو وفي تأسيس السلطة الوطنية الفلسطينية.'
                                    ' 2- شمعون بيريز: كان رئيسًا للوزراء في إسرائيل وقائدًا للمفاوضات الإسرائيلية الفلسطينية خلال فترة أوسلو. '
                                    ' 3-  فهد الحسنات: كان وزيرًا في حكومة الأردن وشارك في التوقيع على اتفاقية السلام بين الأردن والكيان الإسرائيلي المحتل.'
                                    ' 4- حنان عشراوي: كانت واحدة من قادة الحركة الإسلامية في فلسطين، ولعبت دورًا بارزًا في المقاومة ضد الاحتلال الإسرائيلي.'
                                    ' 5- عزت الرشق: كان قائدًا عسكريًا فلسطينيًا بارزًا، ولعب دورًا مهمًا في المقاومة ضد الاحتلال الإسرائيلي '
                                    ' 6- محمود عباس (أبو مازن): شغل مناصب قيادية في منظمة التحرير الفلسطينية وفي السلطة الفلسطينية، وكان له دور بارز في التفاوض وتنفيذ اتفاقية أوسلو.'
                                    ' 7- شيمون بيريس: كان رئيسًا للكيان المحتل وشارك في جهود تحقيق السلام وتحديدًا في توقيع اتفاقية أوسلو.'
                                    ' هؤلاء هم بعض الشخصيات الرئيسية في فلسطين والمنطقة خلال الفترة المشار إليها، وكل واحد منهم كان له تأثير كبير على الأحداث والتطورات في تلك الفترة. ')

async def news3_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' خلال الفترة من عام 1991 إلى 1995، شهدت فلسطين والمنطقة المحيطة بها العديد من الأحداث الهامة، ومن بين هذه الأحداث:'
                                    ' 1- اتفاقية أوسلو (1993): وقعت في سبتمبر 1993 بين منظمة التحرير الفلسطينية وحكومة الاحتلال ، حيث تم تأسيس السلطة الوطنية الفلسطينية وتحديد مسار للسلام والتعاون الثنائي.'
                                    ' 2- عملية السلام بين الأردن وإسرائيل (1994) : تم توقيع معاهدة السلام بين الأردن وإسرائيل في أكتوبر 1994، مما أنهى الحالة الرسمية للحرب بين البلدين.'
                                    ' 3- عملية انتفاضة الأقصى (1994): بدأت هذه الانتفاضة بعد زيارة رئيس الوزراء الإسرائيلي إلى المسجد الأقصى في القدس الشرقية، مما أدى إلى تصاعد التوترات والاشتباكات بين الفلسطينيين والإسرائيليين.'
                                    ' 4- انتخابات المجلس التشريعي الفلسطيني (1996): تم إجراء أول انتخابات ديمقراطية للمجلس التشريعي الفلسطيني في يناير 1996، حيث فازت حركة فتح بأغلبية المقاعد '
                                    ' 5- عملية "جرف الصخر" (1994):  شنت إسرائيل عملية عسكرية واسعة النطاق في قطاع غزة في ديسمبر 1994، ردًا على الهجمات الفلسطينية.'
                                    ' هذه الأحداث تمثل جزءًا من الأحداث الهامة التي وقعت في فلسطين والمنطقة المحيطة بها خلال الفترة من 1991 إلى 1995، وقد ترتب على تلك الأحداث تغيرات كبيرة في الوضع السياسي والأمني في المنطقة.  ')

async def shuhada3_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' خلال الفترة من عام 1991 إلى 1995، فقد العديد من الفلسطينيين حياتهم في مختلف الأحداث والمواجهات. من الصعب تحديد الأسماء بدقة بسبب تعقيدات الوضع السياسي والأمني في تلك الفترة، لكن بعض الشهداء الفلسطينيين الذين استشهدوا في تلك الفترة قد شملوا:'
                                    ' 1- شهداء الانتفاضة الفلسطينية (انتفاضة الحجارة): تم قتل العديد من الفلسطينيين خلال المواجهات مع القوات الإسرائيلية خلال فترة الانتفاضة التي بدأت في عام 1987 واستمرت حتى منتصف التسعينات.'
                                    ' 2- شهداء المواجهات مع القوات الإسرائيلية: تواصلت المواجهات بين الفلسطينيين والقوات الإسرائيلية خلال الفترة المشار إليها، مما أدى إلى استشهاد العديد من الفلسطينيين.'
                                    ' 3- شهداء الاعتقال والاعتداءات الإسرائيلية: كانت هناك حوادث اعتقال واعتداءات إسرائيلية على الفلسطينيين خلال تلك الفترة، وتسببت في استشهاد العديد منهم.'
                                    ' 4- شهداء الهجمات الإسرائيلية على قطاع غزة والضفة الغربية: شن الكيان المحتل عمليات عسكرية وهجمات على المناطق الفلسطينية خلال تلك الفترة، مما أدى إلى استشهاد العديد من الفلسطينيين.'
                                    ' تلك الفترة كانت حافلة بالصراعات والمواجهات، مما أدى إلى فقدان حياة العديد من الفلسطينيين، سواء كانوا مدنيين أو مقاتلين. ')
async def help_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('مرحبا! كيف يمكنني مساعدتك ؟ ')


#responses

def handle_response (text : str) -> str :
    processed: str = text.lower()

    if 'مرحبا' in processed:
        return 'اهلا بك  !'

    if 'كيف حالك' in processed:
        return 'بأفضل حال ومستعد دائما للاجابة على اسئلتك !'

    return 'اعتذر لم اتمكن من فهم ما تحاول قوله ارجوك حاول مجددا ...'

async def handle_message (update: Update, context : ContextTypes.DEFAULT_TYPE):
  message_type: str = update.message.chat.type
  text : str = update.message.text

  print(f'user ({update.message.chat.id}) in {message_type} : "{text}"')

  if message_type == 'group':
      if BOT_USERNAME in text:
          new_text: str = text.replace(BOT_USERNAME,'').strip()
          response : str = handle_response(new_text)
      else:
          return
  else:
      response : str = handle_response(text)

  print('Bot : ', response)
  await  update.message.reply_text(response)

async def error(update: Update, context : ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__' :
    print('starting bot ...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))

    app.add_handler(CommandHandler('characters', characters_command))

    app.add_handler(CommandHandler('news', news_command))
    app.add_handler(CommandHandler('shuhada', shuhada_command))

    app.add_handler(CommandHandler('characters2', characters2_command))
    app.add_handler(CommandHandler('news2', news2_command))
    app.add_handler(CommandHandler('shuhada2', shuhada2_command))

    app.add_handler(CommandHandler('characters3', characters3_command))
    app.add_handler(CommandHandler('news3', news3_command))
    app.add_handler(CommandHandler('shuhada3', shuhada3_command))

    app.add_handler(CommandHandler('help', help_command))
    #messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Erorrs
    app.add_error_handler(error)

    #polls the bot
    print('polling..')
    app.run_polling(poll_interval=3)
